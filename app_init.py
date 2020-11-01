# general libs
import os
import time
import urllib.parse
from dotenv import load_dotenv

# kv-session


# flask
from functools import wraps
from flask import Flask, request, redirect, url_for, render_template, session, jsonify

# API & own lib handling
import nltk
from API import API
from ApiConfig import *

nltk.download('punkt')

# API init
apiConfig = ApiConfig()
API = API(config=apiConfig)

# dotenv config
load_dotenv(verbose=True)

# some Flask specific constants
FLASK_SECRET = os.getenv("FLASK_SECRET")
TIMEZONE = 'Europe/Berlin'
# REDIS_URL = "localhost:5000"
REDIS_URL = "0.0.0.0:5000"


# setting timezone
os.environ['TZ'] = TIMEZONE
time.tzset()


# lib init - not nececarry since everything should
# be done trough the API
collector = apiConfig.collector
processor = apiConfig.processor
sentiment = apiConfig.sentiment
complexity = apiConfig.complexity
google_search = apiConfig.altSources.google_search


# flask app init
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = FLASK_SECRET

# TODO: overcommit_memory redis set
