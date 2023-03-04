import os
import CurrencyRouletteGame
import GuessGame
import MemoryGame
import subprocess
import Utils
import Score


def welcome(name):
    hello_str = f'Hello {name} and welcome to the World of Games (WoG).Here you can find many cool games to play.'
    return hello_str


def load_game():
    print('''Please choose a game to play:'
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer'
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')

    games = {1: 'Memory Game', 2: 'Guess Game', 3: 'Currency Roulette'}
    levels = {1: 'Beginner', 2: 'Amateur', 3: 'Semi-Pro', 4: 'Professional', 5: 'World Class'}

    # while True:
    #     try:
    #         chose = int(input('Choose The Number of The Game Which You Want to Play'))
    #         if chose in games:
    #             break
    #     except ValueError:
    #         print('Input number between 1 - 3')
    #     else:
    #         print('Input number between 1 - 3')

    while True:
        chose = input('Choose The Number of The Game Which You Want to Play')
        if chose.isdigit():
            chose = int(chose)
            if int(chose) in games:
                break
            else:
                print('Input number between 1 - 3')

    while True:
        level = input('Please choose game difficulty from 1 to 5:')
        if level.isdigit():
            level = int(level)
            if int(level) in games:
                break
            else:
                print('Input number between 1 - 3')

    # while True:
    #     try:
    #         level = int(input('Please choose game difficulty from 1 to 5:'))
    #         if level in levels:
    #             break
    #     except ValueError:
    #         print('Input number between 1 - 5')
    #     else:
    #         print('Input number between 1 - 5')

    a = games[chose]
    b = levels[level]
    print(f'Nice choice! Prepare to play {a} in {b} difficulty.')
    current_score = '0'
    if chose == 1:
        win = MemoryGame.play(level)
        if win:
            current_score = Score.add_score(level)
    elif chose == 2:
        win = GuessGame.play(level)
        if win:
            current_score = Score.add_score(level)
    else:
        win = CurrencyRouletteGame.play(level)
        if win:
            current_score = Score.add_score(level)

    while True:
        keep_play = input('Do you want keep playing? 1 for yes 2 for no')
        if keep_play.isdigit():
            if int(keep_play) == 1:
                print(f'Your Score is: {current_score}')
                load_game()
            elif int(keep_play) == 2:
                print('Come play again Next time')
                print(f'your score is: {current_score}')
                break
