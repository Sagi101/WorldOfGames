import random
import requests


def get_money_interval(difficulty, random_num):
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    hamara = data['rates']['ILS']
    print(hamara)
    sum = round(hamara * random_num, 2)
    interval = (sum - (5 - difficulty), sum + (5 - difficulty))
    print(interval)
    return interval


def get_guess_from_user(random_num):
    while True:
        guess = input(f'Try to convert this:{random_num}$ to NIS(₪) - ')
        if guess.replace('.', '', 1).isdigit():
            guess = float(guess)
            break
        print("Invalid input, you must enter a number")
    return guess


def play(difficulty):
    random_num = random.randint(1, 100)
    interval = get_money_interval(difficulty, random_num)
    guess = get_guess_from_user(random_num)
    if guess >= interval[0] and guess <= interval[1]:
        print("You got it!")
        return True
    else:
        print("Not in range, Maybe next time")
        return False

