import os
import random
import time


def generate_sequence(difficulty):
    random_list = random.sample(range(1, 101), difficulty)
    print(random_list, end='')
    time.sleep(5)
    print('\r', end=' ')
    return random_list


def get_list_from_user(difficulty):
    user_list = []
    for i in range(1, difficulty+1):
        num = input('Enter a number to your list')
        if num.isdigit():
            num = int(num)
            user_list.append(num)
        else:
            print('Enter numbers')
    # print(user_list)
    return user_list


def is_list_equal(random_list, user_list):
    random_list.sort()
    user_list.sort()
    print(random_list)
    print(user_list)
    if random_list == user_list:
        return True
    else:
        return False


def play(difficulty):
    random_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    if is_list_equal(random_list, user_list) is True:
        print("Perfect Guess")
        return True
    else:
        print("Try Next Time")
        return False
