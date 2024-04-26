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



def get_relevant_activity(user_preferences, selection, df1, df2, df3):
    # Find the relevant activity type and genre for the selected item
    for activity_type, df in zip(['music', 'books', 'movies'], [df1, df2, df3]):
        if selection in df['name'].tolist():
            genre = df[df['name'] == selection]['genre'].iloc[0]
            return activity_type, genre

    return None, None

# Example usage
selection = 'Daddy Issues'  # Example user selection
activity_type, selected_genre = get_relevant_activity(user_preferences, selection, music_df, book_df, movie_df)
print("Relevant activity type:", activity_type)
print("Genre of the selected activity:", selected_genre)



