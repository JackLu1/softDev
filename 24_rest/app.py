# Jack Lu
# SoftDev1 pd8
# K24 -- A RESTful Journey Skyward
# 2018-11-13

from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

# data = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=VrwXbJ5xLB6mnJMKXu1DhihJBeKlCHer57Lz0lPu")
# info = data.read()
# d = json.loads(info)
# print(d)
# print("THE URL IS")
# print(d['url'])

api_key = "VrwXbJ5xLB6mnJMKXu1DhihJBeKlCHer57Lz0lPu"
url = "https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=VrwXbJ5xLB6mnJMKXu1DhihJBeKlCHer57Lz0lPu"

@app.route('/')
def index():
    data = urllib.request.urlopen(url)
    info = data.read()
    d = json.loads(info)
    img = d['url']
    cs = d['cloud_score']
    t = d['date']
    p = d['resource']['planet']
    
    return render_template("index.html", image=img, cloud=cs, date=t, planet=p)


app.debug = True
app.run()
