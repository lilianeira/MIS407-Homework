"""This module provides the historical weather"""

import requests

# Weather data format defaults to 'us', but
# can be optionally set as 'si' to use
# the International System of Units.

_forecastApiKey = '5e4981d279ea465087d2eec8584e9dcd'

# Lat and Long default to Ames, Iowa
_defaultLat = '42.0307810'
_defaultLng = '-93.6319130'


def _sendRequest(time, lat, lng, format):
    r = requests.get(
        'https://api.forecast.io/forecast/' +
        _forecastApiKey +
        '/' + lat +
        ',' + lng +
        ',' + time +
        '?units='+format
        )
    data = r.json()
    return data


def getSnapshot(time, format='us'):
    """returns all relevant data for specefied time"""
    data = _sendRequest(time, _defaultLat, _defaultLng, format)
    response = {
        'temp': data['currently']['temperature'],
        'windSpeed': data['currently']['windSpeed'],
        'windDir': data['currently']['windBearing'],
        'pressure': data['currently']['pressure'],
        'humidity': data['currently']['humidity']
    }
    return response


def getTemp(time, format='us'):
    """returns temp for specefied time"""
    data = _sendRequest(time, _defaultLat, _defaultLng, format)
    try:
        return data['currently']['temperature']
    except:
        return 'N/A'
        

def getWindSpeed(time, format='us'):
    """returns wind speed for specefied time"""
    data = _sendRequest(time, _defaultLat, _defaultLng, format)
    try:
        return data['currently']['windSpeed']
    except:
        return 'N/A'


def getWindDir(time, format='us'):
    """returns wind direction for specefied time"""
    data = _sendRequest(time, _defaultLat, _defaultLng, format)
    try:
        return data['currently']['windBearing']
    except:
        return 'N/A'


def getPressure(time, format='us'):
    """returns pressure for specefied time"""
    data = _sendRequest(time, _defaultLat, _defaultLng, format)
    try:
        return data['currently']['pressure']
    except:
        return 'N/A'


def getHumidity(time, format='us'):
    """# returns humidity for specefied time"""
    data = _sendRequest(time, _defaultLat, _defaultLng, format)
    try:
        return data['currently']['humidity']
    except:
        return 'N/A'
