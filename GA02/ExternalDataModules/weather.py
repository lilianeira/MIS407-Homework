"""This module pulls weather data from Dark Sky.
The weather data format defaults to 'us'
but can be optionally set as 'si' """


import requests
import datetime

# Weather data format defaults to 'us',
# but can be optionally set as 'si'

_forecastApiKey = '5e4981d279ea465087d2eec8584e9dcd'

# Lat and Long default to Ames, Iowa
_defaultLat = '42.0307810'
_defaultLng = '-93.6319130'


def _sendRequest(lat, lng):
    """send request to API"""
    r = requests.get(
        'https://api.forecast.io/forecast/' +
        _forecastApiKey +
        '/' + lat +
        ',' + lng +
        '?units=us'
        )

    data = r.json()
    return data


# returns all relevant data
def getSnapshot(tomorrow=False):
    """return snapshot of weather data"""
    data = _sendRequest(_defaultLat, _defaultLng)
    if tomorrow:
        response = {
            'max': int(round(data['daily']["data"][1]['temperatureMax'])),
            'min': int(round(data['daily']["data"][1]['temperatureMin'])),
            'summary': data['daily']["data"][1]['summary']
        }
    else:
        response = {
            'temp': int(round(data['currently']['temperature'])),
            'summary': data['currently']['summary'],
            'max': int(round(data['daily']["data"][0]['temperatureMax'])),
            'min': int(round(data['daily']["data"][0]['temperatureMin']))
        }
    return response
