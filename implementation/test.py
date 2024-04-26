import numpy as np
import pandas as pd 

df = pd.read_csv("./datasets/music_data.csv", sep=",")

# Unique genres in the DataFrame
unique_genres = df['track_genre'].unique().tolist()

def contains_happy(emotions_list):
    return 'Frustration' in emotions_list

# Filter DataFrame based on genre and emotions
rock_happy_songs = df[(df['track_genre'] == 'rock') & (df['emotions'].apply(contains_happy))]

# Print the filtered DataFrame
print(rock_happy_songs)
