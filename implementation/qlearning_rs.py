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
# selection = 'Daddy Issues'  # Example user selection
# selection = 'Four Rooms (1995)'
selection = 'Jumanji (1995)'
activity_type, selected_genre = get_relevant_activity(user_preferences, selection, music_df, book_df, movie_df)
print("Relevant activity type:", activity_type)
print("Genre of the selected activity:", selected_genre)


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
    
# Define the environment
n_states = 100  # Number of states in the grid world
n_actions = 36  # Number of possible actions (up, down, left, right)

# Initialize Q-table with zeros
Q_table = np.zeros((n_states, n_actions))

# Define parameters
learning_rate = 0.8
discount_factor = 0.95
exploration_prob = 0.2
epochs = 1000  # Number of training epochs

# Q-learning algorithm
for epoch in range(epochs):
    current_state = np.random.randint(0, n_states)  # Start from a random state

    while True:  # Continue until convergence
        # Choose action with epsilon-greedy strategy
        if np.random.rand() < exploration_prob:
            action = np.random.randint(0, n_actions)  # Explore
        else:
            action = np.argmax(Q_table[current_state])  # Exploit

        # Simulate the environment (move to the next state)
        # For simplicity, move to the next state
        next_state = (current_state + 1) % n_states

        # Define a simple reward function (1 if the epoch ends, 0 otherwise)
        # Here, the epoch ends when the loop reaches the maximum state
        feedback = 'thumbs_up' if np.random.rand() < 0.7 else 'thumbs_down'  # Example performance


        # Get the reward based on the feedback
        reward = get_reward(feedback)

        # Update Q-value using the Q-learning update rule
        Q_table[current_state, action] += learning_rate * \
            (reward + discount_factor *
             np.max(Q_table[next_state]) - Q_table[current_state, action])

        # if reward == 5:  # Break if epoch ends
        #     break
        if feedback == 'thumbs_up' or feedback == 'thumbs_down':
            break

        current_state = next_state  # Move to the next state

# After training, the Q-table represents the learned Q-values
print("Learned Q-table:")
print(Q_table)



def recommend_activities(Q_table, current_state, music_df, book_df, movie_df, num_recommendations=6):
    # Retrieve Q-values for the current state
    q_values = Q_table[current_state]
    
    # Sort the Q-values to get the indices of actions (activities) with the highest Q-values
    sorted_indices = np.argsort(q_values)[::-1][:num_recommendations]
    
    recommended_activities = []
    recommended_names = set()  # To keep track of recommended names
    
    for index in sorted_indices:
        # Map the action index to activity type and genre
        if index < len(music_actions):
            activity_type = 'music'
            selected_genre = music_actions[index].split()[-1]
            recommendations = music_df[music_df['genre'].str.contains(selected_genre, case=False)]['name'].tolist()
        elif index < len(music_actions) + len(book_actions):
            activity_type = 'books'
            selected_genre = book_actions[index - len(music_actions)].split()[-1]
            recommendations = book_df[book_df['genre'].str.contains(selected_genre, case=False)]['name'].tolist()
        else:
            activity_type = 'movies'
            selected_genre = movie_actions[index - len(music_actions) - len(book_actions)].split()[-1]
            recommendations = movie_df[movie_df['genre'].str.contains(selected_genre, case=False)]['name'].tolist()
        
        # Select only one recommendation for each category if available and not already recommended
        if recommendations:
            for recommendation in recommendations:
                if recommendation not in recommended_names:
                    recommended_activities.append((activity_type, selected_genre, recommendation))
                    recommended_names.add(recommendation)
                    break  # Break after adding one recommendation to avoid repetition
    
    return recommended_activities

# Example usage
# current_state = 10  # Example current state
# recommended_activities = recommend_activities(Q_table, current_state, music_df, book_df, movie_df, num_recommendations=6)
# print("Recommended Activities:")
# for index, activity in enumerate(recommended_activities, 1):
#     print(f"{index}. Activity Type: {activity[0]}, Genre: {activity[1]}, Recommendation: {activity[2]}")

def user_interaction(recommended_activities):
    print("Here are some recommended activities:")
    for index, activity in enumerate(recommended_activities, 1):
        print(f"{index}. Activity Type: {activity[0]}, Genre: {activity[1]}, Recommendation: {activity[2]}")
    
    while True:
        try:
            selection = int(input("Enter the number corresponding to your choice (1-6) or 0 to skip: "))
            if selection < 0 or selection > 6:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6 or 0 to skip.")
    
    if selection == 0:
        return 'skip'
    else:
        feedback = input("Did you like the recommendation? (thumbs_up/thumbs_down): ")
        return feedback


def recommend_activities(Q_table, current_state, music_df, book_df, movie_df, num_recommendations=6, previous_recommendations=None):
    # Retrieve Q-values for the current state
    q_values = Q_table[current_state]
    
    # Sort the Q-values to get the indices of actions (activities) with the highest Q-values
    sorted_indices = np.argsort(q_values)[::-1][:num_recommendations]
    
    recommended_activities = []
    recommended_names = set()  # To keep track of recommended names
    
    for index in sorted_indices:
        # Map the action index to activity type and genre
        if index < len(music_actions):
            activity_type = 'music'
            selected_genre = music_actions[index].split()[-1]
            recommendations = music_df[music_df['genre'].str.contains(selected_genre, case=False)]['name'].tolist()
        elif index < len(music_actions) + len(book_actions):
            activity_type = 'books'
            selected_genre = book_actions[index - len(music_actions)].split()[-1]
            recommendations = book_df[book_df['genre'].str.contains(selected_genre, case=False)]['name'].tolist()
        else:
            activity_type = 'movies'
            selected_genre = movie_actions[index - len(music_actions) - len(book_actions)].split()[-1]
            recommendations = movie_df[movie_df['genre'].str.contains(selected_genre, case=False)]['name'].tolist()
        
        # Exclude previous recommendations
        if previous_recommendations:
            recommendations = [activity for activity in recommendations if activity not in previous_recommendations]
        
        # Select only one recommendation for each category if available and not already recommended
        if recommendations:
            for recommendation in recommendations:
                if recommendation not in recommended_names:
                    recommended_activities.append((activity_type, selected_genre, recommendation))
                    recommended_names.add(recommendation)
                    break  # Break after adding one recommendation to avoid repetition
    
    return recommended_activities

def recommend_and_get_feedback(Q_table, current_state, music_df, book_df, movie_df, num_recommendations=6, previous_recommendations=None):
    # Recommend activities
    recommended_activities = recommend_activities(Q_table, current_state, music_df, book_df, movie_df, num_recommendations, previous_recommendations)
    
    # Get user feedback
    user_feedback = user_interaction(recommended_activities)
    
    return recommended_activities, user_feedback



current_state = 10  # Example current state
previous_recommendations = None
while True:
    recommended_activities, user_feedback = recommend_and_get_feedback(Q_table, current_state, music_df, book_df, movie_df, num_recommendations=6, previous_recommendations=previous_recommendations)
    if user_feedback != 'skip':
        # Update previous recommendations
        previous_recommendations = [activity[2] for activity in recommended_activities]
        
        # Update Q-values based on user feedback
        for index, activity in enumerate(recommended_activities, 1):
            action_index = get_action_index(activity[0], activity[1])
            reward = get_reward(user_feedback)
            if index == user_feedback:
                # Increase Q-value for the selected action if feedback is thumbs_up
                Q_table[current_state, action_index] += learning_rate * (reward - Q_table[current_state, action_index])
                # If thumbs_up, adjust Q-values for the same type of activity to reinforce
                for act_type, _, _ in recommended_activities:
                    if act_type == activity[0]:
                        action_idx = get_action_index(act_type, activity[1])
                        Q_table[current_state, action_idx] += learning_rate * (reward - Q_table[current_state, action_idx])
            else:
                Q_table[current_state, action_index] += learning_rate * (-2 - Q_table[current_state, action_index])
    else:
        # Skip action, no need to update Q-values
        previous_recommendations = None
        continue

    # Check if the loop should continue (e.g., user feedback is not 'skip')
    if user_feedback != 'skip':
        # Continue providing recommendations
        continue
    else:
        # Break the loop if user skips
        break
