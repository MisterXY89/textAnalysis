
from newsplease import NewsPlease


class Collector:
    """
    docstring for Collector.
    """

    def __init__(self):
        self.doc = "collect"

    def collect(self, urls):
        articles = NewsPlease.from_urls(urls)
        articlesOutput = []
        for article in articles.items():
            articlesOutput.append(article[1])
        return articlesOutput
