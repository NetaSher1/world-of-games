import time

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 400


def get_user_input(txt):
    return input(f"{txt} ")

def clean_screen2():
    import os
    system = os.name
    if system == 'nt':
        os.system('cls')

    else:
        # For macOS and Linux
        os.system('clear')

def clean_screen():
    print("\r                                   ")


class Game:
    def __init__(self):
        self.difficulty = 2

    def play(self):
        return self.start_game()