
from config import Config

from textblob_de.lemmatizers import PatternParserLemmatizer

config = Config()

collector = config.collector
processor = config.processor
sentiment = config.sentiment
complexity = config.complexity
googleSearch = config.altSources.googleSearch

data = collector.collect(config.urls)
test_data = data[0]


article = processor.process(test_data.maintext, test_data.title)
# print(f"{processor.result.alphaTokens=}")
# print(f"{processor.result.parsed=}")
altSourcesForArticle = googleSearch(" ".join(article.titleNounPhrases))
print(f"{altSourcesForArticle=}")



# _lemmatizer = PatternParserLemmatizer()
# _lemmatizer.lemmatize(" ".join(processor.result.alphaTokens))
