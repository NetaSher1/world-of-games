import freecurrencyapi
import json
from datetime import date,datetime
import os
from random import  randint
from dotenv import load_dotenv





def get_rate_and_date():
    load_dotenv()
    my_key = os.getenv("API_KEY")
    client = freecurrencyapi.Client(my_key)

    result = client.latest(base_currency='USD',currencies=['ILS'])
    result["data"]["date"] = str(date.today())
    with open("./current_exchange_rate.txt", "w+") as file:
        file.write(json.dumps(result))
    return True


def is_file_exist_and_updated():
    check_file = os.path.isfile("./current_exchange_rate.txt")
    if check_file:
        with open("./current_exchange_rate.txt", "r") as file:
            data = file.read()
            data = json.loads(data)
            date_string = data["data"]["date"]
            parsed_date = datetime.strptime(date_string, "%Y-%m-%d").date()
            if parsed_date == date.today():
                return True
            else:
                update = get_rate_and_date()
                return update
    else:
        update = get_rate_and_date()
        return update


def generate_num():
    return randint(1, 100)

def get_money_interval(difficulty, generated_value, rate):
    value = generated_value * rate
    interval = (float(format(value - (5 - difficulty), ".2f")), float(format(value + (5 - difficulty), ".2f")))
    return interval


# def get_guess_from_user(value_to_guess):
#     is_true = True
#     while is_true:
#         try:
#             user_guess = float(input(f"How much is {value_to_guess}$ in ILS? "))
#             is_true = False
#             return user_guess
#         except ValueError:
#             print("input must be an integer!")
#             continue


def check_guess(interval: tuple, user_guess, value_to_guess):
    if user_guess == value_to_guess:
        return True
    elif interval[0] < user_guess < interval[1]:
        return True
    else:
        return False


def get_rate_from_file():
    with open ("./current_exchange_rate.txt","r") as file:
        data = file.read()
        data = json.loads(data)
        return float(format(data["data"]["ILS"], ".2f"))




