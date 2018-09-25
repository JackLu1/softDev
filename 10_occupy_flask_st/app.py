# ZhouLu - Jack Lu, Wei Wen Zhou
# SoftDev pd8
# K10 -- Jinja Tuning
# 2018-09-22

from flask import Flask, render_template
import util.process as process

app = Flask(__name__)

# Root directory with link to table of occupations.
@app.route('/')
def index():
    return '<a href="./occupations">click this</a>'

# Calls buildDict to return the dictionary
# Calls chooseRandom to choose Occupation based on relative percentage
@app.route('/occupations')
def render():
    dict = process.buildDict('./data/occupations.csv')
    return render_template(
            'template.html',
            title = 'Title',
            rand = process.chooseRandom(dict),
            occupations = dict
            )

app.debug = True
app.run()
