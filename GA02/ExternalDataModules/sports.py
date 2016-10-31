'''Pull sports data from Cyclones.com'''
import requests
import re
import feedparser
import time
from subprocess import check_output

uptime = check_output(['uptime'])
print("\n")
print('-------------------------------------------------------------')
print(uptime.strip())
print('-------------------------------------------------------------')
print("\n")

d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?')


def feedparserEntry(parser):
    print("\n" + time.strftime("%a, %b %d %I:%M %p"))
    print("-----------------------------------------\n")
    for post in parser.entries:
        print(post.title + "\n")


def responseBasketballM():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=4')
    menBasketballSchedule = feedparserEntry(d)
    print(menBasketballSchedule)


def responseBasketballW():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=8')
    womenBasketballSchedule = feedparserEntry(d)
    print(womenBasketballSchedule)


def responseCrossCountry():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=5')
    crossCountry = feedparserEntry(d)
    print(crossCountry)


def responseGolfM():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=3')
    womenGolf = feedparserEntry(d)
    print(womenGolf)

def responseGolfW():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=10')
    menGolf = feedparserEntry(d)
    print(menGolf)


def responseFootball():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=1')
    football = feedparserEntry(d)
    print(football)


def responseWrestling():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=17')
    wrestling = feedparserEntry(d)
    print(wrestling)


def responseTrackField():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=6')
    trackField = feedparserEntry(d)
    print(trackField)


def responseSoftball():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=7')
    softball = feedparserEntry(d)
    print(softball)


def responseGymnastics():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=11')
    gymnastics = feedparserEntry(d)
    print(gymnastics)


def responseSoccer():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=12')
    soccer = feedparserEntry(d)
    print(soccer)


def responseSwmming():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=13')
    swimming = feedparserEntry(d)
    print(swimming)


def responseTennis():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=14')
    tennis = feedparserEntry(d)
    print(tennis)


def responseVolleyball():
    d = feedparser.parse('http://www.cyclones.com/calendar.ashx/calendar.rss?sport_id=16')
    volleyball = feedparserEntry(d)
    print(volleyball)
feedparserEntry(d)
