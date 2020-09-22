
from .helper import *
from collections import Counter
from germansentiment import SentimentModel

class Sentiment:
    """
    docstring
    """

    def __init__(self):
        self.model = SentimentModel()

    def getArticleSentiment(self, article):
        # use get sentences method
        sentences = article.split(".")
        sentences = prepareText(sentences)
        result = self.model.predict_sentiment(sentences)
        articleSentimenDict = dict(Counter(result))
        return list(articleSentimenDict.items())[0][0], articleSentimenDict
