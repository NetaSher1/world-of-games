import os
from time import sleep
from Utils import get_user_input
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
def welcome():
    is_true = True
    while is_true:
        user_name = input("Your Name? ")
        if len(user_name) >= 2:
            return (f"Hello {user_name} and welcome to the World of Games (WoG).\n"
                    f"Here you can find many cool games to play."), user_name
        else:
            print("Name must at least two characters long")
            continue


def get_game_choice():
    is_true = True
    while is_true:
        try:
            picked_game = int(get_user_input(config.get("game_txt","game_pick_txt")))
            if 1 <= picked_game <= 3:
                is_true = False
                return picked_game
            else:
                print("Your choice has to be between 1-3 \n")
                continue
        except ValueError:
            print("input must be int! \n")
            sleep(2)
            continue




def get_level_choice():
    is_true = True
    while is_true:
        try:
            game_level = int(get_user_input(config.get("game_txt","difficulty_pick_txt")))
            if 1 <= game_level <= 5:
                is_true = False
                return game_level
            else:
                print("Your choice has to be between 1-5")
                continue

        except ValueError:
            print("input must be int! \n")
            sleep(2)
            continue

def load_game():
    game = get_game_choice()
    level = get_level_choice()
    return game,level