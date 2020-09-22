
import spacy
# textblob-de

class Processor(object):
    """
    docstring for Preprocessor.
    """

    def __init__(self):
        self.nlp = spacy.load("de_core_news_md")

    def tokenize(self, text, lemmatize=True):
        text = self._prepareReplacements(text)
        doc = self.nlp(text)
        for token in doc:
            if str(token.text).isalpha():
                tokens.append(token.lemma_)

    def lemmatize(self, word):
        return self.nlp(word)[0].lemma_


    def _prepareReplacements(self, text):
        text.replace("z.B.", "zum Beispiel")
        return text

    def processPipe(self, sentences):
        for doc in nlp.pipe(texts, disable=["tagger", "parser"]):
            # Do something with the doc here
            print([(ent.text, ent.label_) for ent in doc.ents])

    def _getSentences(self):
        pass

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
