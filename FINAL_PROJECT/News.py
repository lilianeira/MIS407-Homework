'''Get the news'''
import feedparser


feedURL = "http://www.iowastatedaily.com/search/?f=rss"


def feedparserEntry(parser):
    responses = []
    for post in parser.entries:
        thingo = {
            "title": post.title,
            "link": post.link
        }
        responses.append(thingo)
    return responses


def newsPlease():
    """here is some news"""
    d = feedparser.parse(feedURL)
    theNews = feedparserEntry(d)
    return theNews
