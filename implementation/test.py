import pandas as pd


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
# print(book_df)
# Function to give initial recommendations based on user preferences
# def initial_recommendation(user_preferences, df1, df2, df3):
#     recommendations = {}
#     for state, preferences in user_preferences.items():
#         music_recommendations = music_df[music_df['genre'].isin(preferences['music'])]['name'].head(2).tolist()
#         book_recommendations = book_df[book_df['genre'].isin(preferences['books'])]['name'].head(2).tolist()
#         movie_recommendations = movie_df[movie_df['genre'].isin(preferences['movies'])]['name'].head(2).tolist()
        
#         recommendations[state] = {'music': music_recommendations, 'books': book_recommendations, 'movies': movie_recommendations}
    
#     return recommendations

# # Example usage
# initial_recommendations = initial_recommendation(user_preferences, music_df, book_df, movie_df)
# print("Initial recommendations:", initial_recommendations)

# Function to give initial recommendations based on user preferences
def initial_recommendation(user_preferences, df1, df2, df3):
    recommendations = {}
    for state, preferences in user_preferences.items():
        music_recommendations = []
        for genres in preferences['music']:
            music_recommendations.extend(music_df[music_df['genre'].apply(lambda x: any(genre in x for genre in genres))]['name'].head(2).tolist())
        
        book_recommendations = []
        for genres in preferences['books']:
            book_recommendations.extend(book_df[book_df['genre'].apply(lambda x: any(genre in x for genre in genres))]['name'].head(2).tolist())
        
        movie_recommendations = []
        for genres in preferences['movies']:
            movie_recommendations.extend(movie_df[movie_df['genre'].apply(lambda x: any(genre in x for genre in genres))]['name'].head(2).tolist())
        
        recommendations[state] = {'music': music_recommendations, 'books': book_recommendations, 'movies': movie_recommendations}
    
    return recommendations

# Example usage
initial_recommendations = initial_recommendation(user_preferences,  music_df, book_df, movie_df)
print("Initial recommendations:", initial_recommendations)


