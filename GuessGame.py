import random


def generate_number(difficulty):
    secret_number = int(random.randint(1, difficulty))
    return secret_number


def get_guess_from_user(difficulty):
    user_guess = int(input(f'Guess a number between 1 - {difficulty}'))
    return user_guess


def compare_results(user_guess, secret_number):
    if user_guess == secret_number:
        return True
    else:
        return False


def play(level):
    secret_number = generate_number(level)
    user_guess = get_guess_from_user(level)
    if compare_results(user_guess, secret_number) is True:
        print("Lucky Guess")
        return True
    else:
        print("Maybe Next Time")
        return False






