'''Pull sports data from the Ames Trubune'''
import calendar
import feedparser
import datetime


feed = "http://www.public.iastate.edu/~nscentral/news/rss.xml"
d = feedparser.parse(feed)
print (d['feed']['title'])
print (d['feed']['link'])
