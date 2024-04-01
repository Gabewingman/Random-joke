from flask import Flask, render_template
import random

app = Flask(__name__)

# Some example jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts."
]

@app.route('/')
def index():
    # Choose a random joke
    joke = random.choice(jokes)
    return render_template('index.html', joke=joke)

if __name__ == '__main__':
    app.run(debug=True)

