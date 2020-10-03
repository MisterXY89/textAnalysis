
from .helper import *
from collections import Counter
from germansentiment import SentimentModel

class Sentiment:
    """
    Wrapper/Factory for the germansentiment package
    """

    def __init__(self, processor):
		"""
		init sentiment model
		"""
        self.model = SentimentModel()

    def getArticleSentiment(self, sentences):
        """
		returns the dominant sentiment and sentiment distribution
		takes sentences as list as an argument
		"""
        sentences = prepareText(sentences)
        result = self.model.predict_sentiment(sentences)
        articleSentimenDict = dict(Counter(result))
        return list(articleSentimenDict.items())[0][0], articleSentimenDict
