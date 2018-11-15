# Jack Lu
# SoftDev1 pd8
# K25 -- Getting More REST
# 2019-11-14

# stdlib
import json
from urllib import request

# pip install
from flask import Flask, render_template

app = Flask(__name__)

KEY = "f7203425-0a73-4891-904e-37eacfdd230e"
URL_STUB = "https://content.guardianapis.com/search?q=technology&api-key="
URL = URL_STUB + KEY

@app.route('/')
def index():
    # print("------------------------------------------")
    # print(URL)
    # print("------------------------------------------")
    raw = request.urlopen(URL)
    info = raw.read()
    d = json.loads(info)
    # print("------------------------------------------")
    results = d['response']['results']
    # print(type(results[0]))
    # print(results[0])
    # print("------------------------------------------")

    return render_template("index.html", data = results)

app.debug = True
app.run()
