from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from os.path import exists
from flask import Flask, render_template_string
import webbrowser
import threading
app = Flask(__name__)

@app.route('/')
def score_server():
    if exists(SCORES_FILE_NAME):
        file = open(SCORES_FILE_NAME, 'r')
        content = file.read()
    if content:
        template = '<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score">{{ SCORE }}</div></h1></body></html>'
        return render_template_string(template, SCORE=content)
    else:
        template = '<html><head><title>Scores Game</title></head><body><h1><div id="score" style="color:red">{{ error }}</div></h1></body></html>'
        return render_template_string(template, error=BAD_RETURN_CODE)


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000'
    app.run(host='0.0.0.0')
