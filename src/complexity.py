
import spacy
import pyphen
from .helper import prepareText

class TextComplexity:
    """
    determine the linguistic complexity of a text
    using multiple methods
    for a more detailed & complex implementation with
    multiple language support see https://pypi.org/project/readability/
    for practise purposes I implemented the methods on my own and
    will not use this package
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
                if str(token.text).isalpha():
                    tokens.append(token.text)
        return tokens

    def _getSentences(self, text):
        return prepareText(text.split("."), forSentiment=False)

    def _getTotalSyllables(self, words):
        totalSyllables = 0
        for word in words:
            sylString = self.phenDic.inserted(word)
            sylCount = len(sylString.split("-"))
            totalSyllables += sylCount
        return totalSyllables

    def fleschReadingEase(self, text):
        sentences = self._getSentences(text)
        totalSentences = len(sentences)
        words = self._getWords(sentences)
        totalWords = len(words)
        totalSyllables = self._getTotalSyllables(words)
        SL = totalWords/totalSentences
        WL = totalSyllables/totalWords
        return 180 - SL - (WL * 58.5)

    def fleschKincaidGradeLevel(self, text):
        print("> Warning: this implementation does not return useful info for german texts.")
        sentences = self._getSentences(text)
        totalSentences = len(sentences)
        words = self._getWords(sentences)
        totalWords = len(words)
        totalSyllables = self._getTotalSyllables(words)
        return 0.39 * (totalWords/totalSentences) + 11.8 * (totalSyllables/totalWords) - 15.59

    def automatedReadabiltyIndex(self, text):
        print("> Warning: this implementation does not return useful info for german texts.")
        sentences = self._getSentences(text)
        totalSentences = len(sentences)
        words = self._getWords(sentences)
        totalWords = len(words)
        totalChars = len(text)
        return 4.71 * (totalChars/totalWords) + 0.5 * (totalWords/totalSentences) - 21.43
