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

d = feedparser.parse('http://cyclones.com/rss.aspx?path=football')


def feedparserEntry(parser):
    print("\n" + time.strftime("%a, %b %d %I:%M %p"))
    print("-----------------------------------------\n")
    for post in parser.entries:
        print(post.title + "\n")

feedparserEntry(d)
