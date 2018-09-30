# Jack Lu
# SoftDev1 pd8
# K13 -- EchoEchoEcho
# 2018-09-27

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    print(app)
    return render_template('file.html')

@app.route('/auth', methods=["POST"])
def authenticate():
    print(app)
    print(request)
    print(request.form)
    print(request.form['username'])
    print(request.headers)
    usr = request.form['username']
    return render_template('authenticate.html', identity = usr, method = request.method)

app.debug = True
app.run()
