# Jack Lu
# SoftDev1 pd8
# K13 -- EchoEchoEcho
# 2018-09-27

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    print(app)
    link = '<a href="./auth">auth</a>'
    return link + render_template('file.html')

@app.route('/auth')
def authenticate():
    print(app)
    print(request)
    print(request.args)
    print(request.args['username'])
    print(request.headers)
    return "your usename is " + request.args['username']


app.debug = True
app.run()
