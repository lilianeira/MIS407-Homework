'''Pull sports data from the Ames Trubune'''
import calendar
import feedparser
import datetime


feedURL = "http://www.public.iastate.edu/~nscentral/news/rss.xml"
feed = feedparser.parse(feedURL)


def feedparserEntry(parser):
    strr = ""
    now = datetime.datetime.now()
    nowStamp = dateToTimeStamp(now)
    countr = 0
    for post in parser.entries:
        format = '%Y-%m-%d'
        str = post.s_localstartdate[:10]
        newDate = datetime.datetime.strptime(str, format)
        stamp2 = dateToTimeStamp(newDate)
        if stamp2 >= nowStamp and countr < 4:
            countr = countr + 1
            strr = strr + post.title + " in " + post.ev_location + "\n"
    if countr == 0:
        strr = "No headlines are available at this time."

    return strr

def getHeadline(title):
