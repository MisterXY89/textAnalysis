
import json
import spacy
import requests
from io import BytesIO
from base64 import b64encode
from wordcloud import WordCloud
# from textblob_de import PatternParser
from textblob_de import TextBlobDE as TextBlob
from textblob_de.lemmatizers import PatternParserLemmatizer
from textblob_de import PatternTagger, PatternParserNPExtractor

class Processor:
    """
    docstring for Processor
    """

    def __init__(self):
        self.nlp = spacy.load("de_core_news_md")
        self.result = NewsArticle()

    def process(self, maintext, title=""):
        print("> Processing started")
        self.text = maintext
        self.title = title
        self.nlp = spacy.load("de_core_news_md")
        self._lemmatizer = PatternParserLemmatizer()
        self.NPExtractor = PatternParserNPExtractor()
        self.blob = TextBlob(self.text, pos_tagger=PatternTagger(include_punc=True))
        self.result.parsed = self.blob.parse()
        self.result.blob = self.blob
        self.result.sentences = [str(sentence) for sentence in self.blob.sentences]
        self.result.words = self.blob.words
        self.result.tokens = self.blob.tokens
        self.result.alphaTokens = self._makeAlpha(self.result.tokens)
        self.result.lemmas = self._lemmatizer.lemmatize(" ".join(self.result.alphaTokens))
        self.result.tokensWithoutStops = self._remStopWords(" ".join(self.result.alphaTokens)).split(" ")
        self.result.lemmasWithoutStops = self._remStopWords(self.result.lemmas, posLemma=True).split(" ")
        self.result.szFreeSentences = self._removeSZ(self.result.sentences)
        self._genWordCloud(self.result.tokensWithoutStops)
        if title != "":
            self.titleBlob = TextBlob(self.title)
            doc = self.nlp(self.title)
            self.result.titleNounPhrases = [chunk.text for chunk in doc.noun_chunks]
            if len(self.result.titleNounPhrases) <= 0:
                self.result.titleNounPhrases = self._remStopWords(" ".join(self._makeAlpha(self.titleBlob.tokens)))
        return self.result

    def _removeSZ(self, sentences):
        return [sentence.replace("ß", "ss") for sentence in sentences]

    def _remStopWords(self, text, posLemma=False):
        if posLemma:
            lemmas = [el[0] for el in text]
            text = " ".join(lemmas)
        doc = self.nlp(text)
        return " ".join([el.text for el in doc if not el.is_stop])

    def _makeTokenAlpha(self, token):
        accaptableChars = ["-", "*"]
        return "".join([char for char in token if str(char).isalpha() or char in accaptableChars])

    def _makeAlpha(self, tokens):
        return [self._makeTokenAlpha(token) for token in tokens if str(token).isalpha()]

    def _genWordCloud(self, tokens):
        # https://www.file.io/
        # useable only once
        # upload to & use link:
        self.result.wordcloud = WordCloud().generate(" ".join(self.result.tokensWithoutStops))
        self.result.wordcloudImage = BytesIO()
        self.result.wordcloud.to_image().save(self.result.wordcloudImage, 'PNG')
        self.result.wordcloudImage.seek(0)

        self.result.wordcloudImageBase64 = b64encode(self.result.wordcloudImage.read())
        # response = requests.post("https://file.io", files={"file": self.result.wordcloudImage})
        self.result.wordcloudImageUrl = ""
        # if response.status_code == 200:
        #     self.result.wordcloudImageUrl = json.loads(response.text)["link"]



class NewsArticle:
    """
    docstring for NewsArticle
    Object will be returned after processing text,
    contains all info
    """

    def __init__(self):
        self.blob = None
        self.words = None
        self.tokens = None
        self.lemmas = None
        self.entities = None
        self.sentences = None
        self.alphaTokens = None
        self.stopWordFreeText = None
        # self.sentiment = None
        # self.title = None
        # self.maintext = None
        # self.readability = None
