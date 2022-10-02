from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)


@app.route('/')
def guess_the_number():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=400>'


@app.route('/<int:number>')
def guessed_number(number):
    if number > random_number:
        return '<h1 style ="color:red;">Too big! Try again.</h1>' \
           '<img src="https://media.giphy.com/media/UIpzEC5QTvuOQ/giphy.gif" width=300>'
    elif number < random_number:
        return '<h1 style ="color:red;">Too small! Try again.</h1>' \
           '<img src="https://media.giphy.com/media/6uMqzcbWRhoT6/giphy.gif">'
    else:
        return '<h1 style = "color:green;">You Found me...</h1>' \
               '<img src="https://media.giphy.com/media/gyRWkLSQVqlPi/giphy.gif" width=400>'


if __name__ == "__main__":
    app.run(debug=True)