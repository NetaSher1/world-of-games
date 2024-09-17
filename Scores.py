import configparser
import json
import datetime
import os

config = configparser.ConfigParser()
config.read("config.ini")

DIFFICULTY = int(config.get("settings", "difficulty"))
POINTS_OF_WINNING = (DIFFICULTY * 3) + 5

data_struct = {
    "games": {
            "Memory Game": {
                "players": []
            },
            "Guess Game": {
                "players": []
            },
            "Currency Roulette": {
                "players": []
            }
    }
}



def calc_score(difficulty = DIFFICULTY):
    return (difficulty * 3) + 5


def add_score(user_name, game, score):
    if os.path.exists("./consoleGames/score.txt"):
         with open("consoleGames/score.txt", "r+") as f:
            data = json.load(f)

    else:
        data = data_struct.copy()

    data["games"][game]["players"].append(
        {
            "username": str(user_name),
            "score": score,
            "last_session": str(datetime.date.today())
        }
    )
    with open("consoleGames/score.txt", "w") as scorefile:
        scorefile.write(json.dumps(data, indent=4))




