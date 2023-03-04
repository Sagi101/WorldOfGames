from os.path import exists
from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    content = None
    if exists(SCORES_FILE_NAME):
        file = open(SCORES_FILE_NAME, 'r')
        content = file.read()
        file.close()
    if content:
       current_score = int(content) + POINTS_OF_WINNING
    else:
        current_score = POINTS_OF_WINNING
    file = open(SCORES_FILE_NAME, 'w')
    file.write(str(current_score))
    file.close()
    return current_score