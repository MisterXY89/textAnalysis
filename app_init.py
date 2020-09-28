# general libs
import os
import time
import urllib.parse
from dotenv import load_dotenv

# kv-session
import redis
from redis import Redis
from flask_kvsession import KVSessionExtension
from simplekv.memory.redisstore import RedisStore

# flask
from functools import wraps
from flask import Flask, request, redirect, url_for, render_template, session, jsonify

# API & own lib handling
from API import API
from ApiConfig import *

# API init
apiConfig = ApiConfig()
API = API(config=apiConfig)

# dotenv config
load_dotenv(verbose=True)

# some Flask specific constants
FLASK_SECRET = os.getenv("FLASK_SECRET")
TIMEZONE = 'Europe/Berlin'
REDIS_URL = "localhost:5000"


# setting timezone
os.environ['TZ'] = TIMEZONE
time.tzset()


# lib init - not nececarry since everything should
# be done trough the API
collector = apiConfig.collector
processor = apiConfig.processor
sentiment = apiConfig.sentiment
complexity = apiConfig.complexity
googleSearch = apiConfig.altSources.googleSearch


# flask app init
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = FLASK_SECRET


# flask-kv-session init
store = RedisStore(redis.StrictRedis())
KVSessionExtension(store, app)

urllib.parse.uses_netloc.append('redis')
url = urllib.parse.urlparse(REDIS_URL)
conn = Redis(host=url.hostname, port=url.port, db=0, password=url.password)
