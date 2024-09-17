import random

def generate_number(range):
    secret_num = random.randint(1,range * 2 )
    return secret_num

def compare(secret_num: int, user_guess: int):
    secret_num = secret_num
    user_guess = user_guess

    return user_guess == secret_num


