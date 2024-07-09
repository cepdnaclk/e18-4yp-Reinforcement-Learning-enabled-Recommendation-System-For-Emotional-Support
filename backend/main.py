from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import pandas as pd
from hashlib import sha256
import requests
from fuzzywuzzy import fuzz
import random
import numpy as np

app = FastAPI()

books_unique = ["Fiction", "Classics", "Science Fiction", "Historical Fiction", "Horror", "Poetry", "Travel", "Nonfiction", "Comics", "Graphic Novels", "Young Adult", "Mystery", "Crime", "Thriller", "Romance", "Chick Lit", "Art", "Music", "Paranormal", "LGBT", "Children's", "Sports", "Memoir", "Biography", "Religion", "History", "Philosophy", "Self Help", "Psychology", "Business", "Spirituality", "Humor", "Science", "Business", "Religion"]
music_unique = ['alternative', 'blues', 'dance', 'electro', 'electronic', 'folk', 'indie', 'metal', 'new-age', 'pop', 'rock', 'soul', 'world-music']
movie_unique = ["Adventure", "Animation", "Children", "Comedy", "Fantasy", "Romance", "Horror", "Sci-Fi", "Western"]

class User(BaseModel):
    username: str
    email: str
    password: str
    preferences: dict

class UserSignIn(BaseModel):
    username: str
    password: str


def get_user_pref_network(df, user_id):
  user_row = df[(df["user_id"] == user_id)]

  if not user_row.empty:
        user_row = user_row.iloc[0]
        books_preferences = user_row["books_preferences"]
        films_preferences = user_row["film_preferences"]
        music_preferences = user_row["music_preferences"]
  else:
        books_preferences = []
        films_preferences = []
        music_preferences = []

  return books_preferences, films_preferences, music_preferences


def get_state(df, user_id, mental_state):
    user_row = df[(df["user_id"] == user_id) & (df["mental_state"] == mental_state)]

    if not user_row.empty:
            user_row = user_row.iloc[0]
            books_preferences = user_row["books_preferences"]
            films_preferences = user_row["film_preferences"]
            music_preferences = user_row["music_preferences"]
    else:
            books_preferences = []
            films_preferences = []
            music_preferences = []

    return {'user_id': user_id, 'mental_state': mental_state, 'books': books_preferences, 'films': films_preferences, 'music': music_preferences}


def get_matching_value(book, music, film, user_id, data):
    
    book_1, film_1, music_1 = get_user_pref_network(data, user_id)
    book_score = fuzz.token_set_ratio(book, book_1)
    music_score = fuzz.token_set_ratio(music, music_1)
    film_score = fuzz.token_set_ratio(film, film_1)

    return (book_score + music_score + film_score)/3


def get_similar_users(data, user_id, mental_state):
    
    similar_users = []

    for idx, row in data.iterrows():
        if row['mental_state'] == mental_state:
            matching_value = get_matching_value(row['books_preferences'], row['music_preferences'], row['film_preferences'], user_id, data)
            if matching_value > 85:
                similar_users.append(user_id)

    return similar_users


def get_ego_suggestions(similar_users_high, data, mental_state):
  
    data = pd.read_csv('backend\data.csv')
    data = data.fillna('')

    book_suggestions = []
    music_suggestions = []
    film_suggestions = []

    for user_id in similar_users_high:
        user_row = data[(data["user_id"] == user_id) & (data["mental_state"] == mental_state)]
        user_row = user_row.iloc[0]
        book_suggestions.append(user_row['imm_book_sugg'])
        music_suggestions.append(user_row['imm_music_sugg'])
        film_suggestions.append(user_row['imm_movie_sugg'])

    return book_suggestions, music_suggestions, film_suggestions


def get_suggestions_from_user_pref(user_id, book_data, film_data, music_data, mental_state, data):

    max_elements = 100

    state_id = get_state(data, user_id, mental_state)
    book_preferences = state_id['books']
    music_preferences = state_id['music']
    film_preferences = state_id['films']

    books = book_data.loc[book_data['genre'].apply(lambda x: any(g in x for g in book_preferences)), 'name'].tolist()[:max_elements]
    music = music_data.loc[music_data['genre'].apply(lambda x: any(g in x for g in music_preferences)), 'name'].tolist()[:max_elements]
    film = film_data.loc[film_data['genre'].apply(lambda x: any(g in x for g in film_preferences)), 'name'].tolist()[:max_elements]

    return books, music, film

def get_suggestions_from_explore(user_id, book_data, film_data, music_data, mental_state, data):

  max_elements = 100

  state_id = get_state(data, user_id, mental_state)

  exp_book_pref = [item for item in books_unique if item not in state_id['books']]
  exp_music_pref = [item for item in music_unique if item not in state_id['music']]
  exp_film_pref = [item for item in movie_unique if item not in state_id['films']]

  books = book_data.loc[book_data['genre'].apply(lambda x: any(g in x for g in exp_book_pref)), 'name'].tolist()[:max_elements]
  music = music_data.loc[music_data['genre'].apply(lambda x: any(g in x for g in exp_music_pref)), 'name'].tolist()[:max_elements]
  film = film_data.loc[film_data['genre'].apply(lambda x: any(g in x for g in exp_film_pref)), 'name'].tolist()[:max_elements]

  return books, music, film


def clean_list(lst):
    return [item for item in lst if item]


def get_exploit_suggest(ego, usr, ratio):

    suggetion_ego = random.sample(ego, min(ratio, len(ego)))

    if len(suggetion_ego) < ratio:
      balance = ratio - len(suggetion_ego)
      suggetion_usr = random.sample(usr, min(balance, len(usr)))
      return clean_list(suggetion_ego + suggetion_usr)

    return clean_list(suggetion_ego)


@app.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: User):
    # print the json
    print(user.dict())
    data = pd.read_csv(r'backend\data.csv')
    data = data.fillna('')

    if user.username in data['username'].values:
        raise HTTPException(status_code=400, detail="username already exists")

    if user.email in data['email'].values:
        raise HTTPException(status_code=400, detail="Email already exists")

    preferences = user.preferences
    user_id = int(data['user_id'].max()) + 1

    new_user_happy = {
        "user_id": user_id,
        "username": user.username,
        "password": user.password,
        "email": user.email,
        "mental_state": 'happy',
        "books_preferences": str(preferences["books"]["happy"]),
        "music_preferences": str(preferences["music"]["happy"]),
        "film_preferences": str(preferences["movies"]["happy"])
    }

    new_user_relaxed = {
        "user_id": user_id,
        "username": user.username,
        "password": user.password,
        "email": user.email,
        "mental_state": 'relaxed',
        "books_preferences": str(preferences["books"]["relaxed"]),
        "music_preferences": str(preferences["music"]["relaxed"]),
        "film_preferences": str(preferences["movies"]["relaxed"])
    }

    new_user_stressed = {
        "user_id": user_id,
        "username": user.username,
        "password": user.password,
        "email": user.email,
        "mental_state": 'stressed',
        "books_preferences": str(preferences["books"]["stressed"]),
        "music_preferences": str(preferences["music"]["stressed"]),
        "film_preferences": str(preferences["movies"]["stressed"])
    }

    new_user_sad = {
        "user_id": user_id,
        "username": user.username,
        "password": user.password,
        "email": user.email,
        "mental_state": 'sad',
        "books_preferences": str(preferences["books"]["sad"]),
        "music_preferences": str(preferences["music"]["sad"]),
        "film_preferences": str(preferences["movies"]["sad"])
    }


    df_happy = pd.DataFrame([new_user_happy])
    df_relaxed = pd.DataFrame([new_user_relaxed])
    df_stressed = pd.DataFrame([new_user_stressed])
    df_sad = pd.DataFrame([new_user_sad])

    # Concatenate all DataFrames together
    data = pd.concat([data, df_happy, df_relaxed, df_stressed, df_sad], ignore_index=True)
    data.to_csv('backend\data.csv', index=False)

    return {"user_id": user_id, "username": str(user.username)}


@app.post("/signin")
def signin(user: UserSignIn):
    data = pd.read_csv('backend/data.csv')
    data = data.fillna('')
    
    user_data = data[(data['username'] == user.username) & (data['password'] == user.password)]

    if user_data.empty:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    else:
        user_info = user_data.iloc[0]
        return {"user_id": int(user_info['user_id']), "username": str(user_info['username'])}

@app.get("/get-suggestions")
def get_suggestions(user_id: int, username: str, mental_state: str):

    data = pd.read_csv(r'backend\data.csv')
    ratio = pd.read_csv(r'\data.csvratio.csv')
    df_books = pd.read_csv(r'\data.csvbook_filtered_data.csv')
    df_songs = pd.read_csv(r'\data.csvmusic_filtered_data.csv')
    df_movies = pd.read_csv(r'\data.csvmovie_filtered_data.csv')

    book_ratio = int(ratio['book'].values[0])
    film_ratio = int(ratio['film'].values[0])
    music_ratio = int(ratio['music'].values[0])
    
    epsilon = 0.3
    # state_id = get_state(data, int(user_id), mental_state)
    similar_users = get_similar_users(data, int(user_id), mental_state)
    book_ego, music_ego, film_ego = get_ego_suggestions(similar_users, data, mental_state)
    book_usr, music_usr, film_usr = get_suggestions_from_user_pref(int(user_id), df_books, df_movies, df_songs, mental_state, data)
    
    if np.random.rand() < epsilon:
      print('Exploration results')
      book_exp, music_exp, film_exp = get_suggestions_from_explore(user_id, df_books, df_movies, df_songs, mental_state, data)
      book_suggestion = random.sample(book_exp, min(book_ratio, len(book_exp)))
      film_suggestion = random.sample(film_exp, min(film_ratio, len(film_exp)))
      music_suggestion = random.sample(music_exp, min(music_ratio, len(music_exp)))

    else:
      print('Exploitation results')
      book_suggestion = get_exploit_suggest(book_ego, book_usr, book_ratio)
      film_suggestion = get_exploit_suggest(film_ego, film_usr, film_ratio)
      music_suggestion = get_exploit_suggest(music_ego, music_usr, music_ratio)

    
    return {"books": book_suggestion , "films": film_suggestion, "songs": music_suggestion}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)