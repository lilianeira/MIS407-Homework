"""This module pulls weather data from openweathermap.
The weather data format defaults to 'us'
but can be optionally set as 'si' """


import requests

# Weather data format defaults to 'us',
# but can be optionally set as 'si'

_openWeatherApiKey = '84ae7c721ed64a70da9c1ddb07ba7416'

# Lat and Long default to Ames, Iowa
_defaultLat = '42.0307810'
_defaultLng = '-93.6319130'


def _sendRequest(lat, lng, format):
    """send request to API"""
    if format == 'us':
        format = 'imperial'
    elif format == 'si':
        format = 'metric'
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?appid=' +
        _openWeatherApiKey +
        '&lat=' + lat +
        '&lon=' + lng +
        '&units='+format
        )
    data = r.json()
    return data


# returns all relevant data
def getSnapshot(format='us'):
    """return snapshot of weather data"""
    data = _sendRequest(_defaultLat, _defaultLng, format)
    response = {
        'temp': data['main']['temp'],
        'windSpeed': data['wind']['speed'],
        'windDir': data['wind']['deg'],
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity']
    }
    return response


def getTemp(format='us'):
    """returns temp"""
    data = _sendRequest(_defaultLat, _defaultLng, format)
    try:
        return data['main']['temp']
    except:
        return 'N/A'


def getWindSpeed(format='us'):
    """returns wind speed"""
    data = _sendRequest(_defaultLat, _defaultLng, format)
    try:
        return data['wind']['speed']
    except:
        return 'N/A'


def getWindDir(format='us'):
    """returns wind direction"""
    data = _sendRequest(_defaultLat, _defaultLng, format)
    try:
        return data['wind']['deg']
    except:
        return 'N/A'


def getPressure(format='us'):
    """returns pressure"""
    data = _sendRequest(_defaultLat, _defaultLng, format)
    try:
        return data['main']['pressure']
    except:
        return 'N/A'


def getHumidity(format='us'):
    """returns humidity"""
    data = _sendRequest(_defaultLat, _defaultLng, format)
    try:
        return data['main']['pressure']
    except:
        return 'N/A'        
