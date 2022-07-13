from flask import Flask
from random import randint
app = Flask(__name__)


@app.route("/")
def home():
    return '<h1>Guess a number Between 0-9:</h1>' \
           '<img src="https://media.giphy.com/media/JdFEeta1hLNnO/giphy.gif">'

@app.route("/<int:number>")
def guess(number):
    random_num = randint(0, 9)
    if number < random_num:
        return '<h1 style="color:red">Too low.Try again 😃</h1>' \
               '<img src="https://i.giphy.com/media/jD4DwBtqPXRXa/giphy.webp">'
    elif number > random_num:
        return '<h1 style="color: purple">Too high.Try again 😃</h1>' \
               '<img src="https://i.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.webp">'
    elif number == random_num:
        return '<h1 style="color: green">You found it.😁</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
