from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    hello = '<a href="/hello"> hello </a>'
    return "a certain magical index<br>" + hello

@app.route('/hello')
def hello():
    link = '<a href="/hello/go_here"> link </a>'
    return 'hey, please click this ' + link

@app.route('/hello/go_here')
def go_here():
    return 'thanks'
