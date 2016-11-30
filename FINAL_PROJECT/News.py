'''Pull sports data from the Iowa State'''
import feedparser

# Function to fetch the rss feed and return the parsed RSS
def parseRSS( rss_url ):
    return feedparser.parse( rss_url )

# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    headlines = []

    feed = parseRSS( rss_url )
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])

    return headlines
# Funtion to add links to headlines
def getLinks( rss_url ):
    links = []

    feed = parseRSS( rss_url )
    for newsitem in feed['items']:
        links.append(newsitem['link'])
    return links
# A list to hold all headlines
allheadlines = []
alllinks = []
# List of RSS feeds that we will fetch and combine
newsurls = {
    'ISU':           'http://www.public.iastate.edu/~nscentral/news/rss.xml',
}
# Iterate over the feed urls
for key,url in newsurls.items():
    # Call getHeadlines() and combine the returned headlines with allheadlines
    allheadlines.extend( getHeadlines( url ) )
    alllinks.extend( getLinks( url ))

# Iterate over the allheadlines list and print each headline
for hl in allheadlines:
    print(hl)
