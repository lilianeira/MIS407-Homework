'''Pull sports data from Cyclones.com'''
import calendar
import feedparser
import datetime


feedURL = "http://www.cyclones.com/calendar.ashx/calendar.rss"


def dateToTimeStamp(dt):
    """convert a datetime obj to UNIX timestamp"""
    response = calendar.timegm(dt.utctimetuple())
    return response


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
        if stamp2 >= nowStamp:
            countr = countr + 1
            strr = strr + post.title + " in " + post.ev_location + "\n\n"
    if countr == 0:
        strr = "No upcoming events for that sport are scheduled at this time."

    return strr

def getSports(sport):
    if sport == "all":
        response = AllSports()
    elif sport == "Men's Basketball":
        response = BasketballM()
    elif sport == "Cross Country":
        response = CrossCountry()
    elif sport == "Men's Golf":
        response = GolfM()
    elif sport == "Woman's Golf":
        response = GolfW()
    elif sport == "Football":
        response = Football()
    elif sport == "Wrestling":
        response = Wrestling()
    elif sport == "Track and Field":
        response = TrackField()
    elif sport == "Softball":
        response = Softball()
    elif sport == "Gymnastics":
        response = Gymnastics()
    elif sport == "Soccer":
        response = Soccer()
    elif sport == "Swimming":
        response = Swimming()
    elif sport == "Tennis":
        response = Tennis()
    elif sport == "Volleyball":
        response = Volleyball()
    return response

def AllSports():
    d = feedparser.parse(feedURL)
    allsports = feedparserEntry(d)
    return allsports


def BasketballM():
    d = feedparser.parse(feedURL + '?sport_id=4')
    menBasketballSchedule = feedparserEntry(d)
    return menBasketballSchedule


def BasketballW():
    d = feedparser.parse(feedURL + '?sport_id=8')
    womenBasketballSchedule = feedparserEntry(d)
    return womenBasketballSchedule


def CrossCountry():
    d = feedparser.parse(feedURL + '?sport_id=5')
    crossCountry = feedparserEntry(d)
    return crossCountry


def GolfM():
    d = feedparser.parse(feedURL + '?sport_id=3')
    womenGolf = feedparserEntry(d)
    return womenGolf


def GolfW():
    d = feedparser.parse(feedURL + '?sport_id=10')
    menGolf = feedparserEntry(d)
    return menGolf


def Football():
    d = feedparser.parse(feedURL + '?sport_id=1')
    football = feedparserEntry(d)
    return football


def Wrestling():
    d = feedparser.parse(feedURL + '?sport_id=17')
    wrestling = feedparserEntry(d)
    return wrestling


def TrackField():
    d = feedparser.parse(feedURL + '?sport_id=6')
    trackField = feedparserEntry(d)
    return trackField


def Softball():
    d = feedparser.parse(feedURL + '?sport_id=7')
    softball = feedparserEntry(d)
    return softball


def Gymnastics():
    d = feedparser.parse(feedURL + '?sport_id=11')
    gymnastics = feedparserEntry(d)
    return gymnastics


def Soccer():
    d = feedparser.parse(feedURL + '?sport_id=12')
    soccer = feedparserEntry(d)
    return soccer


def Swimming():
    d = feedparser.parse(feedURL + '?sport_id=13')
    swimming = feedparserEntry(d)
    return swimming


def Tennis():
    d = feedparser.parse(feedURL + '?sport_id=14')
    tennis = feedparserEntry(d)
    return tennis


def Volleyball():
    d = feedparser.parse(feedURL + '?sport_id=16')
    volleyball = feedparserEntry(d)
    return volleyball
