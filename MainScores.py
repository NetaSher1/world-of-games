from flask import Flask,render_template
import json
import os
from  Utils import BAD_RETURN_CODE
app = Flask(__name__)

@app.route("/scores")
def score_server():
    if os.path.exists("./consoleGames/score.txt"):
        with open("consoleGames/score.txt", "r") as scorefile:
            scores = json.load(scorefile)
        return render_template("scores.html", scores=scores["games"])
    else:
        message = BAD_RETURN_CODE
        return render_template("scores.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)