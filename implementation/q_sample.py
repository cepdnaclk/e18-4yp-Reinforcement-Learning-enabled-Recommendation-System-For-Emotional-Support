import numpy as np
import pandas as pd

# Mappings from genre/emotion names to integer indices
genre_to_index = {'metal': 0, 'rock': 1, 'pop':2, 'electronic':3, 'electro':4, 'dance':5, 'world-music':6, 'soul':7, 'blues':8, 'alternative':9, 'indie':10,'folk':11}
emotion_to_index = {'Happy': 0, 'Sad': 1, 'Frustration': 2, 'Neutral': 3}

 # Assuming a fixed number of emotions
num_emotions = len(emotion_to_index)

def get_recommendations(genre_index, emotion_index):
    df = pd.read_csv("./datasets/music_data.csv", sep = ",")
    unique_genres = df['track_genre'].unique().tolist()
    unique_emotions = df['emotions'].unique().tolist()

    filtered_data = df[(df['track_genre'] == unique_genres[genre_index]) & (df['emotions'] == unique_emotions[emotion_index])]
    recommendations = filtered_data['track_name'].tolist()

    # Placeholder example: Generate random recommendations
    # recommendations = ['Song 1', 'Song 2', 'Song 3']

    return recommendations

class QLearning:
    def __init__(self, state_space_size, action_space_size, alpha, gamma, epsilon):
        self.state_space_size = state_space_size
        self.action_space_size = action_space_size
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # exploration rate
        self.q_table = np.zeros((state_space_size, action_space_size))

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            # Exploration: choose a random action
            action = np.random.randint(self.action_space_size)
        else:
            # Exploitation: choose the action with the highest Q-value
            action = np.argmax(self.q_table[state])
        return action

    def update_q_table(self, state, action, reward, next_state):
        # Q-learning update rule
        old_q_value = self.q_table[state, action]
        max_next_q_value = np.max(self.q_table[next_state])
        new_q_value = old_q_value + self.alpha * (reward + self.gamma * max_next_q_value - old_q_value)
        self.q_table[state, action] = new_q_value



    def train(self, num_episodes, user_preferences):
        for episode in range(num_episodes):
            # Initialize state
            state = self.get_state(user_preferences)

            while True:
                # Choose action
                action = self.choose_action(state)

                # Execute action and get reward and next state
                reward, next_state = self.execute_action(action)

                # Update Q-value
                self.update_q_table(state, action, reward, next_state)

                # Update state
                state = next_state

                if done:
                    break


    def get_state(self, user_preferences):
        # Convert user preferences to a unique state representation
        # Example: If user_preferences is a dictionary with keys 'genre' and 'emotion':
        genre = user_preferences.get('genre', '')
        emotion = user_preferences.get('emotion', '')

        # Map genre and emotion to integer indices
        genre_index = genre_to_index.get(genre, -1)  # Use -1 if genre is not found in mapping
        emotion_index = emotion_to_index.get(emotion, -1)  # Use -1 if emotion is not found in mapping

        # Concatenate genre and emotion indices to form the state
        if genre_index != -1 and emotion_index != -1:
            state = genre_index * num_emotions + emotion_index
        else:
            # Handle the case when genre or emotion is not found in the mappings
            state = -1  # Use -1 as an indicator of an invalid state

        return state





    def execute_action(self, state):
        # Retrieve recommendations based on the current state
        # Example: If state represents a combination of genre and emotion indices
        genre_index = state // num_emotions
        emotion_index = state % num_emotions

        # Retrieve recommendations for the given genre and emotion
        recommendations = get_recommendations(genre_index, emotion_index)

        return recommendations



state_space_size = 100  
action_space_size = 3  # Recommend music, movie, book
alpha = 0.1
gamma = 0.9
epsilon = 0.1

# Initialize the recommendation system
q_learning_system = QLearning(state_space_size, action_space_size, alpha, gamma, epsilon)

# Train the recommendation system
num_episodes = 1000  
user_preferences = {}  # User preferences data
q_learning_system.train(num_episodes, user_preferences)
