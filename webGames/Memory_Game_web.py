from random import randint


def generate_sequence(difficulty):
    num_list = [randint(1,101) for num in range(difficulty)]
    return num_list

def is_list_equal(generated_list,user_list):
    for i in generated_list:
        if i in user_list:
            continue
        else:
            return False
    return True



