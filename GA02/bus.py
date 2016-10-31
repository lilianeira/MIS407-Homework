import requests
import xml.etree.ElementTree as ET

agency = 'cyride'

def getRouteTimes(stop):
    r = requests.get(
        'http://webservices.nextbus.com/service/publicXMLFeed?'
        'command=predictions' +
        '&a=' + agency +
        '&stopId=' + stop +
        '&useShortTitles=true'
        )
    tree = ET.parse(r)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)
    tree.write(busses.xml)
    return busses.xml
    #data = r.json()
    #return data
