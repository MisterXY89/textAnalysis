
# from gevent import monkey
# monkey.patch_all()

import os
import sys
import json
import time

from config import Config

from functools import wraps
from flask import Flask, request, redirect, url_for, render_template, session, jsonify

config = Config()

collector = config.collector
processor = config.processor
sentiment = config.sentiment
complexity = config.complexity

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = config.FLASK_SECRET


@app.route("/analyse", methods=["POST"])
def analyse():
    data = requests.form
    if "newsURL" in data:
        pass
    else:
        redirect(url_for("error", msg= "Fehlender Parameter <newsURL>"))

@app.route("/error")
def error():
    data = requests.args
    msg = "Bitte versuche es erneut oder eröffne einen Issue auf <a href='#TODO_GH' target='blank_'>GitHub</a>."
    if "msg" in data:
        msg += "<br><code>" + data["msg"] + "</code>"
    render_template("error.html", msg=msg)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')

# newsArticles = col.collect(urls)
# for item in newsArticles:
#     sentimentForItem = sent.getArticleSentiment(item.maintext)
#     # info = wiki.get(item.title)
#     print(f"# {item.title} #")
#     # print(f"{info=}")
#     alts = altSources.googleSearch(item.title)
#     print(f"{alts=}")
#     print(sentimentForItem)
#     readabilityFleshReading = tc.fleschReadingEase(item.maintext)
#     print(f"{readabilityFleshReading=}")
#     print("--------")
