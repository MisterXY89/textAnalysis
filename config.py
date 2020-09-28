
import os
import time
from dotenv import load_dotenv

from src import collector
from src import processor
from src import sentiment
from src import complexity
from src import wikiSearch as wiki
from src import alternativeSources as altSources

load_dotenv(verbose=True)

class Config:
    def __init__(self):
        self.FLASK_SECRET = os.getenv("FLASK_SECRET")
        self.TIMEZONE = 'Europe/Berlin'
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

        # set timezone:
        os.environ['TZ'] = self.TIMEZONE
        time.tzset()
