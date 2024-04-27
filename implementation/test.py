import pandas as pd
import numpy as np



music_genres = ['alternative', 'blues', 'dance', 'electro', 'electronic', 'folk', 'indie', 'metal', 'new-age', 'pop', 'rock', 'soul', 'world-music']
book_genres = ['Romance', 'Travel','Music', 'Poetry', 'Fantasy', 'Historical Fiction', 'Thriller', 'Science Fiction', 'Comics', 'Horror']
movie_genres = ['Family', 'Drama', 'Romance', 'Travel','Musical', 'Fantasy', 'History', 'Action','Sci-Fi', 'Thriller', 'Comedy', 'Adventure', 'Horror']

music_actions = ['Select Music ' + genre for genre in music_genres]
book_actions = ['Select Book ' + genre for genre in book_genres]
movie_actions = ['Select Movie ' + genre for genre in movie_genres]

actions = music_actions + book_actions + movie_actions
# print(len(actions))


def get_user_preferences():
    preferences = {}
    mental_states = ['Happy', 'Sad', 'Frustration', 'Neutral']
    
    for state in mental_states:
        print(f"Please provide your preferences for {state} state:")
        music_pref = input("Enter 2 preferred music genres (comma-separated): ").strip().split(',')
        movie_pref = input("Enter 2 preferred movie genres (comma-separated): ").strip().split(',')
        book_pref = input("Enter 2 preferred book genres (comma-separated): ").strip().split(',')
        
        # Ensure exactly 2 preferences for each category
        while len(music_pref) != 2 or len(movie_pref) != 2 or len(book_pref) != 2:
            print("Please provide exactly 2 preferences for each category.")
            music_pref = input("Enter your preferred music genres (comma-separated): ").strip().split(',')
            movie_pref = input("Enter your preferred movie genres (comma-separated): ").strip().split(',')
            book_pref = input("Enter your preferred book genres (comma-separated): ").strip().split(',')
        
        preferences[state] = {'music': music_pref, 'movies': movie_pref, 'books': book_pref}
    
    return preferences

# Example usage
# user_preferences = get_user_preferences()
user_preferences = {'Happy': {'music': ['Drama', ' Romance'], 'movies': ['Drama', ' Romance'], 'books': ['Drama', ' Romance']}, 'Sad': {'music': ['Drama', ' Romance'], 'movies': ['Drama', ' Romance'], 'books': ['Drama', ' Romance']}, 'Frustration': {'music': ['Drama', ' Romance'], 'movies': ['Drama', ' Romance'], 'books': ['Drama', ' Romance']}, 'Neutral': {'music': ['Drama', ' Romance'], 'movies': ['Drama', ' Romance'], 'books': ['Drama', ' Romance']}}
# print("User preferences:", user_preferences)

book_df = pd.read_csv("./datasets/book_filtered_data.csv", sep = ",")
movie_df = pd.read_csv("./datasets/movie_filtered_data.csv", sep = ",")
music_df = pd.read_csv("./datasets/music_filtered_data.csv", sep = ",")


def get_relevant_suggestions(user_preferences, emotion, df1, df2, df3):
    # Function to get relevant suggestions based on user's emotion
    preferences = user_preferences.get(emotion, {'music': [], 'books': [], 'movies': []})
    
    music_recommendations = []
    for genres in preferences['music']:
        genre_tracks = df1[df1['genre'].apply(lambda x: any(genre in x for genre in genres))]
        for track in genre_tracks['name'].tolist():
            if track not in music_recommendations:
                music_recommendations.append(track)
                break

    book_recommendations = []
    for genres in preferences['books']:
        genre_books = df2[df2['genre'].apply(lambda x: any(genre in x for genre in genres))]
        for book in genre_books['name'].tolist():
            if book not in book_recommendations:
                book_recommendations.append(book)
                break

    movie_recommendations = []
    for genres in preferences['movies']:
        genre_movies = df3[df3['genre'].apply(lambda x: any(genre in x for genre in genres))]
        for movie in genre_movies['name'].tolist():
            if movie not in movie_recommendations:
                movie_recommendations.append(movie)
                break

    return {'music': music_recommendations[:2], 'books': book_recommendations[:2], 'movies': movie_recommendations[:2]}

# Example usage
emotion = 'Sad'  # Example emotion
relevant_suggestions = get_relevant_suggestions(user_preferences, emotion, music_df, book_df, movie_df)
print("Relevant initial suggestions based on emotion:", relevant_suggestions)


def get_relevant_activity(user_preferences, selection, df1, df2, df3):
    # Find the relevant activity type and genre for the selected item
    for activity_type, df in zip(['music', 'books', 'movies'], [df1, df2, df3]):
        if selection in df['name'].tolist():
            genre = df[df['name'] == selection]['genre'].iloc[0]
            return activity_type, genre

    return None, None

# Example usage
selection = 'Daddy Issues'  # Example user selection
# selection = 'Four Rooms (1995)'
# selection = 'Whisperwood'
activity_type, selected_genre = get_relevant_activity(user_preferences, selection, music_df, book_df, movie_df)
print("Relevant activity type:", activity_type)
print("Genre of the selected activity:", selected_genre)




# Define the Q-learning agent class
class QLearningAgent:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table = {}

    def get_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.actions)
        else:
            if state in self.q_table:
                return max(self.q_table[state], key=self.q_table[state].get)
            else:
                return np.random.choice(self.actions)

    def update_q_value(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = {action: 0 for action in self.actions}
        if next_state not in self.q_table:
            self.q_table[next_state] = {action: 0 for action in self.actions}

        max_next_action = max(self.q_table[next_state], key=self.q_table[next_state].get)
        self.q_table[state][action] += self.learning_rate * (
                reward + self.discount_factor * self.q_table[next_state][max_next_action] - self.q_table[state][action])


# Define reward function
def get_reward(feedback):
    if feedback == 'thumbs_up':
        return 5
    elif feedback == 'thumbs_down':
        return -5
    elif feedback == 'skip':
        return -2
    else:
        return 0



# Define states
num_states = 100  # Number of possible states
states = range(num_states)

# Initialize Q-table with zeros
Q = np.zeros((len(states), len(actions)))

# Define learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor


# Q-learning algorithm
def q_learning(state, action_index, reward, next_state):
    next_action_index = np.argmax(Q[next_state])
    Q[state][action_index] += alpha * (reward + gamma * Q[next_state][next_action_index] - Q[state][action_index])



def get_action_index(activity_type, selected_genre):
    if activity_type == 'music':
        action = f"Select Music {selected_genre}"
        if action in music_actions:
            return music_actions.index(action)
    elif activity_type == 'books':
        action = f"Select Book {selected_genre}"
        if action in book_actions:
            return len(music_actions) + book_actions.index(action)
    elif activity_type == 'movies':
        action = f"Select Movie {selected_genre}"
        if action in movie_actions:
            return len(music_actions) + len(book_actions) + movie_actions.index(action)
    return None

# Example usage
action_index = get_action_index(activity_type, selected_genre)
if action_index is not None:
    print("Action index:", action_index)
else:
    print("No action found for the given activity type and genre.")



# Example usage
# Simulate user feedback
state = 0  # Initial state
# action_index = 4  # Example action index (Select Music Genre4)
reward = get_reward('thumbs_up')  # Example reward for thumbs up
next_state = 1  # Next state after user interaction

# Update Q-values based on feedback
q_learning(state, action_index, reward, next_state)

# Recommend next action based on Q-values for the next state
next_state = 1  # Example next state
next_action_index = np.argmax(Q[next_state])
next_action = actions[next_action_index]
print("Next recommended action:", next_action)