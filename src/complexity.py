
import pyphen
from .helper import prepareText
from .processor import Processor

class TextComplexity:
    """
    determine the linguistic complexity of a text
    using multiple methods
    for a more detailed & complex implementation with
    multiple language support see https://pypi.org/project/readability/
    for practise purposes I implemented the methods on my own and
    will not use this package
    """

    def __init__(self, processor):
        self.phenDic = pyphen.Pyphen(lang='de_DE')
        self.processor = processor

    def _getTotalSyllables(self, words):
        """
        get the syllables count for a list of words
        with the pyphen package
        for more see the offical pyphen docs
        """
        totalSyllables = 0
        for word in words:
            sylString = self.phenDic.inserted(word)
            sylCount = len(sylString.split("-"))
            totalSyllables += sylCount
        return totalSyllables

    def fleschReadingEase(self, text):
        """
        calculate the Flesch-Reading-Ease Score for a german text
        takes care of all calculations needed
        TODO: for performance sake add the processor object as param
        """
        article = self.processor.process(text)
        totalSentences = len(article.sentences)
        totalWords = len(article.words)
        totalSyllables = self._getTotalSyllables(article.words)
        SL = totalWords/totalSentences
        WL = totalSyllables/totalWords
        return 180 - SL - (WL * 58.5)

    def fleschKincaidGradeLevel(self, text):
        """
        calculate the Flesch-Kincaid-Grade Level for an ENGLISH TEXT
        takes care of all calculations needed
        WARNING: currently only english texts
        """
        print("> Warning: this implementation does not return useful info for german texts.")
        sentences = self._getSentences(text)
        totalSentences = len(sentences)
        words = self._getWords(sentences)
        totalWords = len(words)
        totalSyllables = self._getTotalSyllables(words)
        return 0.39 * (totalWords/totalSentences) + 11.8 * (totalSyllables/totalWords) - 15.59

    def automatedReadabiltyIndex(self, text):
        """
        calculate the automated Readabilty-Index for an ENGLISH TEXT
        takes care of all calculations needed
        WARNING: currently only english texts
        """
        print("> Warning: this implementation does not return useful info for german texts.")
        sentences = self._getSentences(text)
        totalSentences = len(sentences)
        words = self._getWords(sentences)
        totalWords = len(words)
        totalChars = len(text)
        return 4.71 * (totalChars/totalWords) + 0.5 * (totalWords/totalSentences) - 21.43
