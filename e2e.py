from MainScores import url
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service():

    mydriver = webdriver.chrome()
    mydriver.get(url)
    score = mydriver.find_element(By.ID, 'score')
    score = int(score.text)
    if 1 < score < 1000:
        return True
    else:
        return False

def main_function():
    if test_scores_service():
        return 0
    else:
        return -1
