import requests
import xml.etree.ElementTree as ET

#next bus api requires agency
#this would be public transport agencies
agency = 'cyride'

_nextBusXMLAPIKey = 22

#creates request and generates XML document of bus routes
def getRouteTimes(stop):
    r = requests.get(
        'http://webservices.nextbus.com/service/publicXMLFeed?'
        'command=predictions' +
        '&a=' + agency +
        '&stopId=' + stop +
        '&useShortTitles=true'
        )
    answers = []
    tree = ET.fromstring(r.content)
    #this begins parsing and extracting data from the XML
    for child in tree:
        if child.tag != "Error":
            routeName = child.attrib["routeTitle"]
            routeDescrip = ""
            predictions = []
            #grabs data from XML and assigns them
            #to appropriate time intervals and routes
            for child2 in child:
                routeDescrip = child2.attrib["title"]
                for child3 in child2:
                    if int(child3.attrib["minutes"]) <= 15:
                        predic = {
                            "min": child3.attrib["minutes"],
                            "bus": child3.attrib["vehicle"]
                            }
                        predictions.append(predic)
            entry = {
                "route": routeName,
                "descrip": routeDescrip,
                "predictions": predictions
            }

            if len(predictions) > 0:
                answers.append(entry)
    return answers
