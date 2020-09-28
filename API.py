
import validators

class API:
	"""
	simple interface to use all
	the web app's functionalities
	"""

	def __init__(self, collector=False, processor=False, sentiment=False, complexity=False, altSources=False):
		if not collector:
			self._init_external_API()
		else:
			self._init_Flask_API(collector, processor, sentiment, complexity, altSources)

	def _init_Flask_API(self, collector, processor, sentiment, complexity, altSources):
		self.collector = collector
		self.processor = processor
		self.sentiment = sentiment
		self.complexity = complexity
		self.altSources = altSources

	def _init_external_API(self):
		import config as cf
		# from config import Config
		config = cf.Config(importAPI=False)
		self.collector = config.collector
		self.processor = config.processor
		self.sentiment = config.sentiment
		self.complexity = config.complexity
		self.googleSearch = config.altSources.googleSearch

	def _areValidUrls(self, urls):
		for url in urls:
			print(validators.url(url))
			if not validators.url(url):
				return False
		return True

	def newsAnalysis(self, urls):
		if not self._areValidUrls(urls):
			return "Please provide a valid URL (list)"

		articleData = self.collector.collect(urls)[0]
		maintext = articleData.maintext
		article = self.processor.process(maintext, articleData.title)
		articleComplexity = self.complexity.fleschReadingEase(maintext)
		articleSentiment, articleSentimentDict = self.sentiment.getArticleSentiment(article.sentences)
		try:
			altSourcesForArticle = self.googleSearch(" ".join(article.titleNounPhrases))
		except Exception as e:
			print(f"Error for: {article.titleNounPhrases=}")
			altSourcesForArticle = self.googleSearch(articleData.title)

		renderArticle = {
			"meta" : {
				"date_publish" : articleData.date_publish,
				"date_download" : articleData.date_download,
				"url" : articleData.url,
				"image_url" : articleData.image_url,
				"authors" : articleData.authors
			},
			"title" : articleData.title,
			"maintext" : articleData.maintext,
			"complexity" : articleComplexity,
			"comeplexityType" : "fleschReadingEase",
			"sentiment" : articleSentiment,
			"sentimentDict" : articleSentimentDict,
			"totalWords" : len(article.words),
			"totalSentences" : len(article.sentences),
			"alternativeSources" : altSourcesForArticle,
			# "wordcloudImageUrl" : article.wordcloudImageUrl
			"wordcloudImageBase64": article.wordcloudImageBase64
		}
		return renderArticle
