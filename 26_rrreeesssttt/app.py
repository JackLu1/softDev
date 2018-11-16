# Jack Lu
# SoftDev1 pd8
# Kxx -- hwname
# 201x-xx-xx

# stdlib
import json
from urllib import request
import random

# pip install
from flask import Flask, render_template

# custom modules

app = Flask(__name__)

# 2072 comics exist as of 2018-11-16

# print("-------------------------------------------------------------")
# print(d)
# for i in d:
#     print(str(i) + " : " + str(d[i]))
# print("-------------------------------------------------------------")
def get_json(URL):
    raw = request.urlopen(URL)
    info = raw.read()
    j = json.loads(info)
    return j 

@app.route('/')
def index():
    URL = "https://dog.ceo/api/breeds/list/all"
    doglist = get_json(URL)
    doge = random.choice(list(doglist['message']))

    URL = "https://dog.ceo/api/breed/" + doge + "/images/random"
    dog = get_json(URL)
    dogpic_arg = dog['message']

    URL = "http://xkcd.com/" + str(random.randint(1,2072)) + "/info.0.json"
    xkcd = get_json(URL)
    date_arg = xkcd["year"] + "-" + xkcd["month"] + "-" + xkcd["day"]
    img_arg = xkcd['img']
    title_arg = xkcd['safe_title']

    URL = "https://www.poemist.com/api/v1/randompoems"
    poems = get_json(URL)

    poem_arg = random.choice(list(poems))
    return render_template('index.html', date = date_arg, img=img_arg, title=title_arg, dogpic = dogpic_arg, poem=poem_arg)


app.debug = True
app.run()
