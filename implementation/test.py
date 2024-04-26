import pandas as pd
import numpy as np


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


# # Function to give initial recommendations based on user preferences
# def initial_recommendation(user_preferences, df1, df2, df3):
#     recommendations = {}
#     for state, preferences in user_preferences.items():
#         music_recommendations = []
#         for genres in preferences['music']:
#             music_recommendations.extend(music_df[music_df['genre'].apply(lambda x: any(genre in x for genre in genres))]['name'].head(2).tolist())
        
#         book_recommendations = []
#         for genres in preferences['books']:
#             book_recommendations.extend(book_df[book_df['genre'].apply(lambda x: any(genre in x for genre in genres))]['name'].head(2).tolist())
        
#         movie_recommendations = []
#         for genres in preferences['movies']:
#             movie_recommendations.extend(movie_df[movie_df['genre'].apply(lambda x: any(genre in x for genre in genres))]['name'].head(2).tolist())
        
#         recommendations[state] = {'music': music_recommendations, 'books': book_recommendations, 'movies': movie_recommendations}
    
#     return recommendations

# # Example usage
# initial_recommendations = initial_recommendation(user_preferences,  music_df, book_df, movie_df)
# print("Initial recommendations:", initial_recommendations)

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



# Define states, actions, and initial Q-table
states = range(100)  # Sample 100 states
actions = ['musics', 'movies', 'books']  # Select preferences: music, movies, books
Q = np.zeros((len(states), len(actions)))  # Initialize Q-table with zeros

# Define reward function
def get_reward(feedback):
    if feedback == 'thumbs_up':
        return 5
    elif feedback == 'thumbs_down':
        return -5
    elif feedback == 'skip':
        return -2
    else:
        return -0

# Define learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor

# Q-learning algorithm
def q_learning(state, action_index, reward, next_state):
    next_action_index = np.argmax(Q[next_state])
    Q[state][action_index] += alpha * \
        (reward + gamma * Q[next_state][next_action_index] - Q[state][action_index])

# Example usage
def recommend_next_activity(emotion_index):
    state = emotion_index  # Set initial state based on emotion index
    action_index = np.argmax(Q[state])  # Select action with highest Q-value
    action = actions[action_index]
    return action

# Example: Simulate user feedback (thumbs up, thumbs down, skip)
feedback = 'thumbs_up'  # Example feedback
reward = get_reward(feedback)

# Update Q-values based on feedback
next_state = 0  # Example next state
q_learning(0, 0, reward, next_state)  # Update Q-value

# Get recommendation for next activity
next_emotion_index = 1  # Example next emotion index
next_action = recommend_next_activity(next_emotion_index)
print("Next recommended action:", next_action)
