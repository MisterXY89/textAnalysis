
import validators
import ApiConfig as cf

class API:
	"""
	simple interface to use all
	the web app's functionalities
	"""

	def __init__(self, config = None):
		"""
		constructor:

		optionally load apiConfig for external (non-flask) API use
		via the config param
		"""
		if config == None:
			config = cf.ApiConfig()

		self.collector = config.collector
		self.processor = config.processor
		self.sentiment = config.sentiment
		self.complexity = config.complexity
		self.googleSearch = config.altSources.googleSearch

	def _areValidUrls(self, urls):
		"""
		verify if list of urls are valid
		via the validators package
		"""
		for url in urls:
			if not validators.url(url):
				return False
		return True

	def newsAnalysis(self, urls, valid=False):
		"""
		! currently only the first url is analyzed

		perform a complete analysis -
		bringing together all implemented techniques

		if you are sure that your url is valid set valid = True
		-> this option is used for Flask app (url gets checked via JS)
		"""
		if not valid: # if urls have already been validated
			if not self._areValidUrls(urls):
				return "Please provide a valid URL (list)"

		# collect data
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

		# prepare return dictionary
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
