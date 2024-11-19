from flask import Flask
from random import randint

app = Flask(__name__)
counting_gif_url = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
correct_guess_gif_url = "https://media0.giphy.com/media/b1o4elYH8Tqjm/200.webp?cid=ecf05e47o5gxc15oc1n2wtvnyph5650o1lxdt7q2c3gjzwm8&rid=200.webp&ct=g"
too_low_guess_gif_url = "https://media3.giphy.com/media/LKW8LLAoc1Rcc/200w.webp?cid=ecf05e47iiisnlt4r65l1ci9oco14n1698luxysjdk99rfo3&rid=200w.webp&ct=g"
too_high_guess_gif_url = "https://media0.giphy.com/media/3o6ZtaO9BZHcOjmErm/200.webp?cid=ecf05e471xa3sh9laf2bi8eriay7e8ok1d3dkjtia8k80ijq&rid=200.webp&ct=g"
random_number = randint(1, 9)


@app.route("/")
def hello_world():
    return f"<p>Guess a number 1-9:</p><img src='{counting_gif_url}'/>"


@app.route("/<int:guess>")
def render_guess_page(guess):
    if guess < 1 or guess > 9:
        return "Guess invalid.  Try again."
    elif guess == random_number:
        return f"<p>You guessed correctly!</p><img src='{correct_guess_gif_url}'/>"
    elif guess < random_number:
        return f"<p>Too low!  Try again!</p><img src='{too_low_guess_gif_url}'/>"
    else:
        return f"<p>Too high!</p><img src='{too_high_guess_gif_url}'/>"
