
import os
import time

from src import collector
from src import sentiment
from src import complexity
from src import wikiSearch as wiki
from src import alternativeSources as altSources

class Config:
    def __init__(self):
        self.FLASK_SECRET = "$1$LOMT9Hq5$N.nvua5/7kzMMbKoIhwv21"
        self.TIMEZONE = 'Europe/Berlin'
        # some test urls
        self.urls = [
            "https://www.sueddeutsche.de/wirtschaft/bahn-milliarden-ausbau-1.5029830",
            "https://www.bild.de/regional/saarland/saarland-news/corona-verstoesse-in-saarlouis-polizei-macht-shisha-bar-dicht-72886644.bild.html",
            "https://www.sueddeutsche.de/leben/aktuell-klokultur-1.5035940",
            "https://www.sueddeutsche.de/sport/schalke-04-wagner-1.5039548"
        ]
        self.col = collector.Collector()
        self.sent = sentiment.Sentiment()
        self.tc = complexity.TextComplexity()

        # set timezone:
        os.environ['TZ'] = self.TIMEZONE
        time.tzset()
