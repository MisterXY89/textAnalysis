
from .helper import *
from collections import Counter
from germansentiment import SentimentModel

class Sentiment:
    """
    docstring
    """

    def __init__(self, processor):
        self.model = SentimentModel()
        self.processor = processor

    def getArticleSentiment(self, sentences):
        # use get sentences method
        # sentences = article.split(".")
        sentences = prepareText(sentences)
        result = self.model.predict_sentiment(sentences)
        articleSentimenDict = dict(Counter(result))
        return list(articleSentimenDict.items())[0][0], articleSentimenDict
