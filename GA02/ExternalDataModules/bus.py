import requests

agency = 'cyride'

_nextBusXMLAPIKey = 22

def getRouteTimes(stop,route):
    r = requests.get(
        'http://webservices.nextbus.com/service/publicXMLFeed?'
        'command=predictions' +
        '&a=' + agency +
        '&stopId=' + stop +
        '&r=' + route +
        '&useShortTitles=true'
        )
    data = r.json()
    return data
