"""
Flask Router

@author: Tilman Kerl
@version: 2020.09
"""

from flask import request, redirect, url_for, render_template, session
from app_init import app, API

import redis
from redis import Redis
from flask_kvsession import KVSessionExtension
from simplekv.memory.redisstore import RedisStore


# flask-kv-session init
store = RedisStore(redis.StrictRedis())
KVSessionExtension(store, app)

# urllib.parse.uses_netloc.append('redis')
# url = urllib.parse.urlparse(REDIS_URL)
conn = Redis(host='redis', port=6379, decode_responses=True) #, db=0, password=url.password)

@app.route('/test')
def test():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

@app.route("/analyse", methods=["POST"])
def analyse():
    """
    Analyse the article for the given "newsURL",
    if param not given -> return error
    store results in kv-session
    """
    data = request.form
    if not "newsURL" in data:
        return redirect(url_for("error", msg= "Fehlender Parameter *newsURL in analyse POST"))
    url = data["newsURL"]
    article = API.news_analysis([url], valid=True)
    session["renderArticle"] = article

    return redirect(url_for("result", renderArticle="session"))


@app.route("/result")
def result():
    """
    displays the results from the analysis
    needs the "renderArticle" param to make sure
    that the analysis has been performed &
    that the session isset
    """
    data = request.args
    if not "renderArticle" in data:
        return redirect(url_for("error", msg= "Fehlender Parameter *article in result"))
    article = session["renderArticle"]
    return render_template("result.html", article=article)


@app.route("/error")
def error():
    """
    error route, displays error messages
    optional msg param for extra message
    """
    data = request.args
    msg = "Bitte versuche es erneut oder eröffne einen Issue auf " \
          "<a href='#TODO_GH' target='blank_'>GitHub</a>."
    if "msg" in data:
        msg += "<br><code>" + data["msg"] + "</code>"
    return render_template("error.html", msg=msg)


@app.route("/")
def index():
    """
    standard route
    """
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
