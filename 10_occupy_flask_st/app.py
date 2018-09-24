# ZhouLu - Jack Lu, Wei Wen Zhou
# SoftDev pd8
# K10 -- Jinja Tuning
# 2018-09-22

from flask import Flask, render_template
import csv
import random

app = Flask(__name__)

    # Builds a dictionary of careers occupations and percentage of US workforce.
dict = {}
with open('./data/occupations.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile)
    first = reader.__next__() # Processes column labels Job Class, Percentage
    dict[first[0]] = first[1]
    for i in reader:
        dict[ i[0] ] = float( i[1])

# Choose random job based on percentage
jobList = list(dict.keys())
chanceList = list(dict.values())

@app.route('/')
def index():
    return '<a href="./occupations">click this</a>'

@app.route('/occupations')
def render():
    randJob = random.choices(jobList[1:-1], chanceList[1:-1])[0]
    return render_template(
            'template.html',
            title = 'Title',
            rand = randJob,
            occupations = dict
            )

app.debug = True
app.run()
