from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    link = '<a href="./occupations">go here</a>'
    return link

@app.route('/occupations')
def occupy():
    return render_template(
            'template.html',
            foo='./data/occupations.csv')
