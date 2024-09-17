from flask import Flask,request,jsonify,render_template,session,redirect
from webGames import Guess_Game_web as gg
from webGames import Memory_Game_web as mg
from webGames import Currency_Roulette_Game_web as cr
import configparser
from webGames import Scores
import os
import json
from Utils import BAD_RETURN_CODE

app = Flask(__name__)
app.secret_key = "1a2e3r"
config = configparser.ConfigParser()
config.read("config.ini")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        difficulty = request.form.get('difficulty')
        if difficulty is not None:
            session['difficulty'] = difficulty
        else:
            difficulty = int(config.get("settings","difficulty"))
            session['difficulty'] = difficulty

        # Store the values in session variables
        session['user_name'] = user_name
        session['difficulty'] = difficulty
    return render_template("Main.html")

@app.route("/scores/")
def score_server():
    if os.path.exists("./webGames/score.txt"):
        with open("./webGames/score.txt", "r") as scorefile:
            scores = json.load(scorefile)
        return render_template("scores.html", scores=scores["games"])
    else:
        message = BAD_RETURN_CODE
        return render_template("scores.html", message=message)


@app.route("/guessingGame",methods=['GET','POST'])
def guessing():
    if "score" not in session:
        session["score"] = 0

    secret_num = gg.generate_number(int(session['difficulty']))
    if request.method == 'GET':
        return render_template('Guess_Game.html', difficulty= int(session['difficulty']), score=session['score'])

    elif request.method == 'POST':
        user_guess = int(request.form['guess'])
        secret_num = secret_num

        if gg.compare(secret_num, user_guess):
            message = "Congratulations! You guessed the number!"
            session['score'] += Scores.calc_score()

        else:
            message = f"Sorry, that's not correct. The number was {secret_num}."
            if session["score"] > 0:
                Scores.add_score(user_name=session['user_name'],game="Guess Game",score=int(session["score"]))
            session["score"] = 0

        return render_template('Guess_Game.html', message=message, difficulty=int(session['difficulty']))


@app.route('/memoryGame', methods=['GET','POST'])
def play_memory_game():

    if "score" not in session:
        session["score"] = 0

    difficulty = int(session['difficulty'])

    if request.method == "GET":
        sequence = mg.generate_sequence(difficulty)
        session["sequence"]= sequence
        return render_template('Memory_Game.html', generated_sequence=sequence,difficulty=difficulty,score=session['score'])

    if request.method == "POST":
        user_guess = [int(request.form[f"user_guess{i}"]) for i in range(difficulty)]

        if session["sequence"] == user_guess:
            message = "Congratulations! You guessed the number!"
            session['score'] += Scores.calc_score()
        else:
            message = f"Sorry, that's not correct."
            if session["score"] > 0:
                Scores.add_score(user_name=session['user_name'], game="Memory Game", score=int(session["score"]))
            session["score"] = 0

        return render_template('Memory_Game.html', message=message,difficulty=difficulty)


@app.route("/currencyRoulette", methods=['GET','POST'])
def paly_currency_roulette():
    if "score" not in session:
        session["score"] = 0

    difficulty = int(session['difficulty'])
    if request.method == "GET":
        value_to_guess = cr.generate_num()
        session["value_to_guess"] = value_to_guess
        return render_template('Currency_Roulette.html', value_to_guess=value_to_guess)

    if request.method == "POST":
        rate = cr.get_rate_from_file()
        interval = cr.get_money_interval(difficulty=difficulty, generated_value=int(session["value_to_guess"]), rate=rate)
        user_guess = int(request.form["user_guess"])
        is_guess_correct = cr.check_guess(interval=interval, user_guess=user_guess, value_to_guess=int(session["value_to_guess"]))
        if is_guess_correct:
            message = "You are correct!!!"
            session['score'] += Scores.calc_score()
            return render_template('Currency_Roulette.html', message = message)
        else:
            message = "Wrong!!!"
            if session["score"] > 0:
                Scores.add_score(user_name=session['user_name'], game="Currency Roulette", score=int(session["score"]))
            session["score"] = 0

            return render_template('Currency_Roulette.html', message=message)


@app.route("/currencyRoulette_load")
def get_current_rate():
    is_ready = cr.is_file_exist_and_updated()
    print(is_ready)
    if is_ready:
        return redirect("/currencyRoulette")
    return jsonify({'status': 'not_ready'})

@app.route('/reset')
def reset():
    # Clear all session variables
    session.pop('score', None)
    return redirect('/')

@app.route('/reset_all')
def reset_all():
    # Clear all session variables
    session.clear()
    return redirect('/')
# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
