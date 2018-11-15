# Jack Lu
# SoftDev1 pd8
# Kxx -- hwname
# 201x-xx-xx

# stdlib
import json
from urllib import request

# pip install
from flask import Flask, render_template

# custom modules

app = Flask(__name__)

URL = "https://api.jikan.moe/v3/search/anime/1/episodes"

raw = request.urlopen(URL)
info = raw.read()
d = json.loads(info)
print("-------------------------------------------------------------")
for i in d:
    print(i + " : " + d[i])
print("-------------------------------------------------------------")

@app.route('/')
def jikan():
    return "index"


app.debug = True
app.run()
