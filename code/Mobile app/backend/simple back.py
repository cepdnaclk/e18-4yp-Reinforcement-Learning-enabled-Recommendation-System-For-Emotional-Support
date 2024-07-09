from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == 'test' and password == 'test':
        return jsonify({'message': 'Login successful', 'username': username, 'userid': 1}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/signup', methods=['POST'])
def signup():
    # print the json
    print(request.get_json())
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    return jsonify({'message': 'Signup successful'}), 200

@app.route('/get-suggestions', methods=['POST'])
def get_suggestions():
    data = request.get_json()
    userid = data.get('userid')
    emotion = data.get('emotion')

    # Here you can implement any logic based on userid and emotion
    # For simplicity, we'll return a static set of suggestions

    suggestions = {
        "movies": ["Movie 1", "Movie 2", "Movie 3"],
        "music": ["Music 1", "Music 2", "Music 3"],
        "books": ["Book 1", "Book 2", "Book 3"]
    }

    return jsonify(suggestions=suggestions), 200

@app.route('/update-preference', methods=['POST'])
def update_preference():
    data = request.get_json()
    userid = data.get('userid')
    suggestion = data.get('suggestion')

    # For simplicity, we're just going to print out the suggestion and userid
    # In a real application, you would update the user's preferences in a database
    print(f"Updating preference for user {userid} with suggestion {suggestion}")

    return jsonify(message='Preference updated',userid = 1), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
