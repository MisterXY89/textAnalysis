
import wikipedia as wiki

wiki.set_lang("de")

def getSummary(term):
    return wiki.summary(term)

def get(title):
    terms = title.split(" ")
    pages = []
    for term in terms:
        foundPages = wiki.search(title)
        if len(foundPages) > 0:
            page = foundPages[0]
            sum = wiki.summary(page)
            pages.append(sum)
        # print(dir(page))
        # print(res.summary)
    return pages


# get("Deutsche Bahn erhöht Ticketpreise")
