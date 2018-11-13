# Jack Lu
# SoftDev1 pd8
# K24 -- A RESTful Journey Skyward
# 2018-11-13

from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

#a = urllib.request("https://api.nasa.gov/planetary/apod?api_key=wzy2AkA8Cnw5tbnAoyo0pnI95w0Ot6QM2tV9OkTQ")
d = json.loads("https://api.nasa.gov/planetary/apod?api_key=wzy2AkA8Cnw5tbnAoyo0pnI95w0Ot6QM2tV9OkTQ")
#print(d)

@app.route('/')
def index():
    return "index"

app.debug = True
app.run()
