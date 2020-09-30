
from googlesearch import search

LIMIT = 10

def google_search(title, limit=LIMIT):
    urls = []
    # TODO: add title to return for better display
    for url in search(title, stop=limit):
        urls.append(url)
    return urls
