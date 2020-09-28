
import os
import time
import urllib.parse
from dotenv import load_dotenv


import redis
from redis import Redis
from flask_kvsession import KVSessionExtension
from simplekv.memory.redisstore import RedisStore

from functools import wraps
from flask import Flask, request, redirect, url_for, render_template, session, jsonify



load_dotenv(verbose=True)

class Config:

	def __init__(self, importAPI=True):

		from src import collector
		from src import processor
		from src import sentiment
		from src import complexity
		from src import wikiSearch as wiki
		from src import alternativeSources as altSources

		self.importAPI = importAPI

		# some test urls
		self.urls = [
			"https://www.sueddeutsche.de/wirtschaft/bahn-milliarden-ausbau-1.5029830",
			"https://www.bild.de/regional/saarland/saarland-news/corona-verstoesse-in-saarlouis-polizei-macht-shisha-bar-dicht-72886644.bild.html",
			"https://www.sueddeutsche.de/leben/aktuell-klokultur-1.5035940",
			"https://www.sueddeutsche.de/sport/schalke-04-wagner-1.5039548"
		]


		self.collector = collector.Collector()
		self.processor = processor.Processor()
		self.sentiment = sentiment.Sentiment(self.processor)
		self.complexity = complexity.TextComplexity(self.processor)
		self.altSources = altSources

		if self.importAPI:

			from API import API

			self.API = API(self.collector, self.processor, self.sentiment, self.complexity, self.altSources)

			self.FLASK_SECRET = os.getenv("FLASK_SECRET")
			self.TIMEZONE = 'Europe/Berlin'
			self.REDIS_URL = "localhost:5000"

			# set timezone:
			os.environ['TZ'] = self.TIMEZONE
			time.tzset()


config = Config()

if config.importAPI:
	collector = config.collector
	processor = config.processor
	sentiment = config.sentiment
	complexity = config.complexity
	googleSearch = config.altSources.googleSearch

	API = config.API

	app = Flask(__name__)
	app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
	app.secret_key = config.FLASK_SECRET

	store = RedisStore(redis.StrictRedis())
	KVSessionExtension(store, app)

	urllib.parse.uses_netloc.append('redis')
	url = urllib.parse.urlparse(config.REDIS_URL)
	conn = Redis(host=url.hostname, port=url.port, db=0, password=url.password)
