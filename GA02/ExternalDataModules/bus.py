import requests
import xml.etree.ElementTree as ET

agency = 'cyride'

_nextBusXMLAPIKey = 22

def getRouteTimes(stop):
    r = requests.get(
        'http://webservices.nextbus.com/service/publicXMLFeed?'
        'command=predictions' +
        '&a=' + agency +
        '&stopId=' + stop +
        '&useShortTitles=true'
        )
    data = r.json()
    return data
