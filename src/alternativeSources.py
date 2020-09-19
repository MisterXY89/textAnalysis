

from googlesearch import search

LIMIT = 10

def googleSearch(title, limit=LIMIT):
    urls = []
    for url in search(title, stop=limit):
        urls.append(url)
    return urls
