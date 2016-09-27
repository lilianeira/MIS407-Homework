"""This module pulls weather data from openweathermap.
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


_lastRequest = {
    'si': 0,
    'us': 0
}


_snapShot = {
    'si': {},
    'us': {}
}


def timeSinceLastRequest(format):
    now = datetime.datetime.now()
    nowStamp = int(now.timestamp())
    lastRequest = _lastRequest[format]
    return nowStamp - lastRequest


def _sendRequest(lat, lng, format):
    """send request to API"""
    r = requests.get(
        'https://api.forecast.io/forecast/' +
        _forecastApiKey +
        '/' + lat +
        ',' + lng +
        '?units='+format
        )

    data = r.json()
    try:
        snapshot = {
            'temp': data['currently']['temperature'],
            'windSpeed': data['currently']['windSpeed'],
            'windDir': data['currently']['windBearing'],
            'pressure': data['currently']['pressure']
        }
        _snapShot[format] = snapshot
        dateobj = datetime.datetime.now()
        _lastRequest[format] = int(dateobj.timestamp())
    except:
        snapshot = {
            'temp': 'N/A',
            'windSpeed': 'N/A',
            'windDir': 'N/A',
            'pressure': 'N/A'
        }

    return data


# returns all relevant data
def getSnapshot(format='us'):
    """return snapshot of weather data"""
    data = _sendRequest(_defaultLat, _defaultLng, format)
    response = {
        'temp': data['currently']['temperature'],
        'windSpeed': data['currently']['windSpeed'],
        'windDir': data['currently']['windBearing'],
        'pressure': data['currently']['pressure'],
        'humidity': data['currently']['humidity']
    }
    return response


def getTemp(format='us'):
    """returns temp"""
    timeSince = timeSinceLastRequest(format)
    if timeSince <= 60:
        return _snapShot[format]['temp']
    else:
        data = _sendRequest(_defaultLat, _defaultLng, format)
        try:
            return data['currently']['temperature']
        except:
            return 'N/A'


def getWindSpeed(format='us'):
    """returns wind speed"""
    timeSince = timeSinceLastRequest(format)
    if timeSince <= 60:
        return _snapShot[format]['windSpeed']
    else:
        data = _sendRequest(_defaultLat, _defaultLng, format)
        try:
            return data['currently']['windSpeed']
        except:
            return 'N/A'


def getWindDir(format='us'):
    """returns wind direction"""
    timeSince = timeSinceLastRequest(format)
    if timeSince <= 60:
        return _snapShot[format]['windDir']
    else:
        data = _sendRequest(_defaultLat, _defaultLng, format)
        try:
            return data['currently']['windBearing']
        except:
            return 'N/A'


def getPressure(format='us'):
    """returns pressure"""
    timeSince = timeSinceLastRequest(format)
    if timeSince <= 60:
        return _snapShot[format]['pressure']
    else:
        data = _sendRequest(_defaultLat, _defaultLng, format)
        try:
            return data['currently']['pressure']
        except:
            return 'N/A'
