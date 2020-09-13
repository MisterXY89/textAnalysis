
from src import collector
from src import sentiment
from src import complexity


# "https://www.sueddeutsche.de/politik/klimakrise-klimawandel-freiheit-werkstatt-demokratie-interview-1.4625111",
# "https://www.bild.de/regional/hannover/hannover-aktuell/guth-verliert-stichwahl-kestner-ist-neuer-afd-chef-in-niedersachsen-72888092.bild.html",
# "https://www.bild.de/news/ausland/news-ausland/usa-angreifer-schiesst-cops-in-streifenwagen-nieder-trump-fordert-todesstrafe-72887984.bild.html"
# "https://www.bild.de/news/inland/news-inland/coronavirus-aktuell-deutschland-astrazenca-setzt-impfstoffstudie-wieder-fort-70411946.bild.html",

urls = [
    "https://www.sueddeutsche.de/wirtschaft/bahn-milliarden-ausbau-1.5029830",
    "https://www.bild.de/regional/saarland/saarland-news/corona-verstoesse-in-saarlouis-polizei-macht-shisha-bar-dicht-72886644.bild.html"
]

# 'authors', 'date_download', 'date_modify', 'date_publish', 'description', 'filename', 'get_dict', 'get_serializable_dict', 'image_url', 'language', 'lo
# calpath', 'maintext', 'source_domain', 'text', 'title', 'title_page', 'title_rss', 'url']
col = collector.Collector()
sent = sentiment.Sentiment()
tc = complexity.TextComplexity()

newsArticles = col.collect(urls)
for item in newsArticles:
    sentimentForItem = sent.getArticleSentiment(item.maintext)
    print(f"# {item.title} #")
    # print(item.maintext)
    print("--------")
    print(sentimentForItem)
    readabilityFleshReading = tc.fleschReadingEase(item.maintext)
    readabilityFleshKincaid = tc.fleschKincaidGradeLevel(item.maintext)
    readabilityARI = tc.automatedReadabiltyIndex(item.maintext)
    print(f"{readabilityFleshReading=}")
    print(f"{readabilityFleshKincaid=}")
    print(f"{readabilityARI=}")
