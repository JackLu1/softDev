# - Jack Lu, Hui Min Wu
# SoftDev1 pd8
# K14 -- Do I Know You?
# 2018-10-1

from flask import Flask, render_template, request, session, url_for, redirect
import os

app = Flask(__name__)

# Hardcoded:
usr = 'ZhouLu'
pw = 'abc1234'
# Generate random secret key
app.secret_key = os.urandom(32)

@app.route('/')
def index():
    if usr in session:
        return render_template('welcome.html', title='Welcome ' + usr, user_welcome= usr)
    return render_template('form.html', title='Login')

@app.route('/auth', methods=["POST"])
def authenticate():
    check_usr = request.form["name"] 
    check_pw = request.form["pass"]

    if check_pw != pw and check_usr != usr:
        return render_template('error.html',
            title='Error',
            error_message='Incorrect login information')

    # add username to session
    session[usr] = pw
    return redirect(url_for('index'))

@app.route('/logout', methods=["POST"])
def logout():
    session.pop(usr)
    return redirect(url_for('index'))

app.debug = True
app.run()
