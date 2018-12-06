# import sys
import markov
from flask import Flask, render_template

APP = Flask(__name__)

source = "hunchback.txt"

@APP.route('/', methods=['GET', 'POST'])
def index():
    final_sentence = markov.main(source)
    return render_template('index.html', final_sentence=final_sentence)

if __name__ == '__main__':

    index()
