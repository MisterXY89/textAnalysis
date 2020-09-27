
from gevent import monkey
monkey.patch_all()

import os
import sys
import json
import time

from config import Config

import redis
from flask_kvsession import KVSessionExtension
from simplekv.memory.redisstore import RedisStore

from functools import wraps
from flask import Flask, request, redirect, url_for, render_template, session, jsonify

config = Config()

collector = config.collector
processor = config.processor
sentiment = config.sentiment
complexity = config.complexity
googleSearch = config.altSources.googleSearch

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = config.FLASK_SECRET


store = RedisStore(redis.StrictRedis())
KVSessionExtension(store, app)

@app.route("/analyse", methods=["POST"])
def analyse():
    data = request.form
    if not "newsURL" in data:
        return redirect(url_for("error", msg= "Fehlender Parameter *newsURL in analyse POST"))

    articleData = collector.collect([data["newsURL"]])[0]
    maintext = articleData.maintext
    article = processor.process(maintext, articleData.title)
    articleComplexity = complexity.fleschReadingEase(maintext)
    articleSentiment, articleSentimentDict = sentiment.getArticleSentiment(article.sentences)
    try:
        altSourcesForArticle = googleSearch(" ".join(article.titleNounPhrases))
    except Exception as e:
        print(f"Error for: {article.titleNounPhrases=}")
        altSourcesForArticle = googleSearch(articleData.title)

    wordcloud = article.wordcloudImage
    print(wordcloud)

    renderArticle = {
        "meta" : {
            "date_publish" : articleData.date_publish,
            "date_download" : articleData.date_download,
            "url" : articleData.url,
            "image_url" : articleData.image_url,
            "authors" : articleData.authors
        },
        "title" : articleData.title,
        "maintext" : articleData.maintext,
        "complexity" : articleComplexity,
        "comeplexityType" : "fleschReadingEase",
        "sentiment" : articleSentiment,
        "sentimentDict" : articleSentimentDict,
        "totalWords" : len(article.words),
        "totalSentences" : len(article.sentences),
        "alternativeSources" : altSourcesForArticle,
        "wordcloudImageUrl" : article.wordcloudImageUrl,
        "wordcloudImageBase64": article.wordcloudImageBase64
    }

    session["renderArticle"] = renderArticle

    return redirect(url_for("result", renderArticle="session", wordcloudImageBase64=article.wordcloudImageBase64))

@app.route("/result")
def result():
    data = request.args
    if not "renderArticle" in data:
        return redirect(url_for("error", msg= "Fehlender Parameter *article in result"))
    wordcloudImageBase64 = str(data["wordcloudImageBase64"])
    article = session["renderArticle"]
    return render_template("result.html", article=article, wordcloudImageBase64=wordcloudImageBase64)

@app.route("/error")
def error():
    data = request.args
    msg = "Bitte versuche es erneut oder eröffne einen Issue auf <a href='#TODO_GH' target='blank_'>GitHub</a>."
    if "msg" in data:
        msg += "<br><code>" + data["msg"] + "</code>"
    return render_template("error.html", msg=msg)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
