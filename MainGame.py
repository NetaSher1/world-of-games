from Live import welcome,load_game
from consoleGames.Currency_Roulette_Game import CurrencyRoulette
from consoleGames.Guess_Game import GuessGame
from consoleGames.Memory_Game import MemoryGame
from time import sleep
import Scores

get_user = welcome()
print(get_user[0])
user_name = get_user[1]
print("\n")
user_pick = load_game()

score = 0
keep_playing = True
while keep_playing:
    match user_pick[0]:
        case 1:
            sleep(2)
            game = MemoryGame(user_pick[1])
            game_name = str(game)
            game = game.play()
            print(game)
            if game:
                score += Scores.calc_score(difficulty=user_pick[1])
            keep_playing = game

        case 2:
            sleep(2)
            game = GuessGame(user_pick[1])
            game_name = str(game)
            game = game.play()
            print(game)
            if game:
                score += Scores.calc_score(difficulty=user_pick[1])
            keep_playing = game

        case 3:
            sleep(2)
            game = CurrencyRoulette(user_pick[1])
            game_name = str(game)
            game = game.play()
            print(game)
            if game:
                score += Scores.calc_score(difficulty=user_pick[1])
            keep_playing = game

if score == 0:
    print("You Lose!!")
else:
    Scores.add_score(user_name=user_name,game= game_name, score=score)
