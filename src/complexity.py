
import spacy
import pyphen
from .helper import prepareText

class TextComplexity:
    """
    determine the linguistic complexity of a text
    using multiple methods
    """

    def __init__(self):
        self.nlp = spacy.load("de_core_news_md")
        self.phenDic = pyphen.Pyphen(lang='de_DE')

    def _getWords(self, sentences):
        # words = tokens
        tokens = []
        for sentence in sentences:
            doc = self.nlp(sentence)
            for token in doc:
                if str(token.text).isalpha() and not token.is_stop:
                    tokens.append(token.text)
        return tokens

    def _getSentences(self, text):
        return prepareText(text.split("."), forSentiment=False)

    def _getTotalSyllables(self, words):
        totalSyllables = 0
        for word in words:
            totalSyllables += len(self.phenDic.inserted(word).split("-"))
        return totalSyllables

    def fleschReadingEase(self, text):
        sentences = self._getSentences(text)
        totalSentences = len(sentences)
        words = self._getWords(sentences)
        totalWords = len(words)
        totalSyllables = self._getTotalSyllables(words)
        return 206.835 - 1.015 * (totalWords/totalSentences) - 84.6 * (totalSyllables/totalWords)

    def fleschKincaidGradeLevel(self, text):
        sentences = self._getSentences(text)
        totalSentences = len(sentences)
        words = self._getWords(sentences)
        totalWords = len(words)
        totalSyllables = self._getTotalSyllables(words)
        return 0.39 * (totalWords/totalSentences) + 11.8 * (totalSyllables/totalWords) - 15.59
        # return (0.39 * len(text.split()) / len(text.split('.')) ) + 11.8 * ( sum(list(map(lambda x: 1 if x in ["a","i","e","o","u","y","A","E","I","O","U","y"] else 0,text))) / len(text.split())) - 15.59

    def automatedReadabiltyIndex(self, text):
        sentences = self._getSentences(text)
        print(sentences)
        totalSentences = len(sentences)
        words = self._getWords(sentences)
        totalWords = len(words)
        totalChars = len(text)
        return 4.71 * (totalChars/totalWords) + 0.5 * (totalWords/totalSentences) - 21.43
