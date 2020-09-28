# German news text mining and analysis

Some work in progress playground for text mining and analysis techniques
applied to the German language.

Namely:
 - language/textual complexity, see Toni Amstad's dissertations (thx to u/toikpi)<br>
  there is a good introductory article here: https://medium.com/analytics-vidhya/visualising-text-complexity-with-readability-formulas-c86474efc730
 - sentiment analysis, see Oliver Guhr
 - WordCloud generation
 - potential aternative sources collection
 - [TODO] summary of texts
 - [TODO] topic modeling
 - [TODO] opinion mining

## API
I've outsourced the analysis part to the `API.py` file, thus providing an interface to the functionalities of the web app without having to use it.

### Usage
```python

from API import API
api = API()
# urls is of type list, but currently only the first url will be analyzed
results = api.newsAnalysis(urls)
```
The resulting dict has the form (for [this](https://www.n-tv.de/politik/politik_kommentare/Trump-ist-kein-Putschist-sondern-Opportunist-article22057804.html) article):
```json

{
   "meta":{
      "date_publish":datetime.datetime(2020, 9, 24, 18, 16, 58),
      "date_download":datetime.datetime(2020, 9, 28, 17, 12, 6),
      "url":"https://www.n-tv.de/politik/politik_kommentare/Trump-ist-kein-Putschist-sondern-Opportunist-article22057804.html",
      "image_url":"https://bilder4.n-tv.de/img/incoming/crop22057823/5921323742-cImg_16_9-w1200/8d54447978b902ac4a8e248333154280.jpg",
      "authors":[
         "Roland Peters"
      ]
   },
   "title":"Machterhalt mit Gewalt? Trump ist kein Putschist, sondern Opportunist",
   "maintext":"Wird US-Präsident Trump sich weigern, eine Wahlniederlage zu akzeptieren? Sind die Vereinigten Staaten...",
   "complexity":50.49290780141844,
   "comeplexityType":"fleschReadingEase",
   "sentiment":"neutral",
   "sentimentDict":{
      "neutral":36,
      "negative":2,
      "positive":1
   },
   "totalWords":611,
   "totalSentences":39,
   "alternativeSources":[
      "https://www.n-tv.de/politik/politik_kommentare/Trump-ist-kein-Putschist-sondern-Opportunist-article22057804.html",
      "http://press24.net/news/25707594/machterhalt-mit-gewalt-trump-ist-kein-putschist-sondern-opportunist",
      "https://newstral.com/de/article/de/1160824251/machterhalt-mit-gewalt-trump-ist-kein-putschist-sondern-opportunist",
      "https://www.tagesschau.de/ausland/biden-proteste-usa-101.html",
      "https://www.tagesschau.de/ausland/trump-portland-proteste-101.html",
      "https://www.finanzen100.de/aktien/sqn-asset-finance-inc-fd-ltd-registered-shares-pr-c-wkn-a2jmq3_H1712320553_138182446/",
      "https://www.deutschlandfunkkultur.de/the-lincoln-project-us-republikaner-gegen-trump.1005.de.html?dram:article_id=480915",
      "https://www.zdf.de/nachrichten/politik/trump-proteste-demokraten-uswahl-102.html",
      "https://www.spiegel.de/politik/ausland/usa-wie-donald-trump-die-gewalt-auf-den-strassen-nutzt-podcast-acht-milliarden-a-5b46af45-c4a5-40cc-abf9-f28ce49c1f55",
      "https://www.handelsblatt.com/politik/international/proteste-in-den-usa-trump-bezeichnet-ausschreitungen-in-kenosha-als-inlaendischen-terrorismus/26149492.html"
   ],
   "wordcloudImageBase64":b"...oOwrBPb8N4OQmSxWhyRy84kMAw3tAGEiPUvb5QmIwwvftrifDexiU1sYhOb2MQmNrGJTWxiE5sogf8DE2NcVihW9rIAAAAASUVORK5CYII="
}
```

## Libraries
 I'm using:
 - spacy & nltk for common NLP tasks
 - NewsPlease for fetching news articles by their url
 - pyphen for syllables interaction
 - germansentiment for the sentiment analysis

## A general link/resource collection
I'm using this mainly for me, so I have a place to save potential useful stuff :D
- https://medium.com/idealo-tech-blog/common-pitfalls-with-the-preprocessing-of-german-text-for-nlp-3cfb8dc19ebe
- https://medium.com/@umerfarooq_26378/text-summarization-in-python-76c0a41f0dc4


## References


`Guhr, Oliver, et al. "Training a Broad-Coverage German Sentiment Classification Model for Dialog Systems." Proceedings of The 12th Language Resources and Evaluation Conference. 2020.`

`Hamborg, Felix, et al. "News-please: a generic news crawler and extractor." 15th International Symposium of Information Science (ISI 2017). 2017.`

`Amstad, Toni. Wie verständlich sind unsere Zeitungen?. Studenten-Schreib-Service, 1978.`
