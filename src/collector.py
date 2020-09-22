
from newsplease import NewsPlease


class Collector:
    """
    docstring for Collector.
    """

    def __init__(self):
        self.doc = "collect"

    def collect(self, urls):
        # 'authors', 'date_download', 'date_modify', 'date_publish', 'description', 'filename', 'get_dict', 'get_serializable_dict', 'image_url', 'language', 'lo
        # calpath', 'maintext', 'source_domain', 'text', 'title', 'title_page', 'title_rss', 'url']
        articles = NewsPlease.from_urls(urls)
        articlesOutput = []
        for article in articles.items():
            articlesOutput.append(article[1])
        return articlesOutput
