"""This module provides the historical weather"""

import requests

# Weather data format defaults to 'us', but
# can be optionally set as 'si' to use
# the International System of Units.

_forecastApiKey = '5e4981d279ea465087d2eec8584e9dcd'

# Lat and Long default to Ames, Iowa
_defaultLat = '42.0307810'
_defaultLng = '-93.6319130'


# Store session data here to lower
# amount of requests required (potentially)
_dataUS = {}
_dataSI = {}


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
    try:
        snapshot = {
            'temp': data['currently']['temperature'],
            'windSpeed': data['currently']['windSpeed'],
            'windDir': data['currently']['windBearing'],
            'pressure': data['currently']['pressure']
        }
    except:
        snapshot = {
            'temp': 'N/A',
            'windSpeed': 'N/A',
            'windDir': 'N/A',
            'pressure': 'N/A'
        }
    if format == 'us':
        _dataUS[time] = snapshot
    else:
        _dataSI[time] = snapshot
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
    if format == 'us':
        helperDict = _dataUS
    else:
        helperDict = _dataSI
    if time in helperDict:
        return helperDict[time]['temp']
    else:
        data = _sendRequest(time, _defaultLat, _defaultLng, format)
        try:
            return data['currently']['temperature']
        except:
            return 'N/A'


def getWindSpeed(time, format='us'):
    """returns wind speed for specefied time"""
    if format == 'us':
        helperDict = _dataUS
    else:
        helperDict = _dataSI
    if time in helperDict:
        return helperDict[time]['windSpeed']
    else:
        data = _sendRequest(time, _defaultLat, _defaultLng, format)
        try:
            return data['currently']['windSpeed']
        except:
            return 'N/A'


def getWindDir(time, format='us'):
    """returns wind direction for specefied time"""
    if format == 'us':
        helperDict = _dataUS
    else:
        helperDict = _dataSI
    if time in helperDict:
        return helperDict[time]['windDir']
    else:
        data = _sendRequest(time, _defaultLat, _defaultLng, format)
        try:
            return data['currently']['windBearing']
        except:
            return 'N/A'


def getPressure(time, format='us'):
    """returns pressure for specefied time"""
    if format == 'us':
        helperDict = _dataUS
    else:
        helperDict = _dataSI
    if time in helperDict:
        return helperDict[time]['pressure']
    else:
        data = _sendRequest(time, _defaultLat, _defaultLng, format)
        try:
            return data['currently']['pressure']
        except:
            return 'N/A'
