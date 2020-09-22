
import spacy
 from textblob_de import TextBlobDE as TextBlob

class Processor:
    """
    docstring for Preprocessor.
    """

    def __init__(self, text):
        self.text = text
        self.nlp = spacy.load("de_core_news_md")
        self.blob = TextBlob(text)
        self.sentences = self.blob.sentences
        self.words = self.blob.words
        self.tokens = self.blob.tokens
        print(f"{self.words=}")
        print(f"{self.tokens=}")
        self.lemmas = blob.tokens.lemmatize()
        self.alphaTokens = self.makeAlpha(self.tokens)


    def makeAlpha(self, text):
        alphaTokens = []
        for token in tokens:
            if str(token).isalpha():
                alphaTokens.append(token)
        return alphaTokens


class NewsArticle:
    """
    docstring for NewsArticle
    Object will be returned after processing text,
    contains all info
    """

    def __init__(self):
        self.tokens = 0
        self.sentences = 0
        self.sentimen = ""
        self.title = ""
        self.maintext = ""
        self.stopWordFreeText = ""
        self.readability = ""
        self.entities = []
