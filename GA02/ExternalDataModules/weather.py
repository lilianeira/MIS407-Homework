"""This module pulls weather data from Dark Sky."""


import requests


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


def tomorrow():
    """return tomorrow's weather"""
    data = _sendRequest(_defaultLat, _defaultLng)
    try:
        response = {
            'max': int(round(data['daily']["data"][1]['temperatureMax'])),
            'min': int(round(data['daily']["data"][1]['temperatureMin'])),
            'summary': data['daily']["data"][1]['summary']
        }
    except:
        response = {"Error": True}
    return response


def today():
    """return today's weather"""
    data = _sendRequest(_defaultLat, _defaultLng)
    try:
        response = {
            'temp': int(round(data['currently']['temperature'])),
            'summary': data['currently']['summary'],
            'max': int(round(data['daily']["data"][0]['temperatureMax'])),
            'min': int(round(data['daily']["data"][0]['temperatureMin']))
        }
    except:
        response = {"Error": True}
    return response
