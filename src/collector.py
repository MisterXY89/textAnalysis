
from newsplease import NewsPlease


class Collector:
    """
    Wrapper/Factory for newsplease
    """

    def __init__(self):
        self.doc = "collect"

    def collect(self, urls):
		"""
		returns list of newsplease objects
		containing the following attrs:
		'authors', 'date_download', 'date_modify', 'date_publish', 'description', 'filename', 'get_dict', 'get_serializable_dict', 'image_url', 'language', 'lo
        calpath', 'maintext', 'source_domain', 'text', 'title', 'title_page', 'title_rss', 'url'
		for more see the NewsPlease docs
		"""
        articles = NewsPlease.from_urls(urls)
        articles_output = []
        articles_output_append = articles_output.append
        for article in articles.items():
            articles_output_append(article[1])
        return articles_output
