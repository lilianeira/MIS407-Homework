
import requests

# Weather data format defaults to 'us',
# but can be optionally set as 'si'

_openWeatherApiKey = '84ae7c721ed64a70da9c1ddb07ba7416'

# Lat and Long default to Ames, Iowa
_defaultLat = '42.0307810'
_defaultLng = '-93.6319130'


def _sendRequest(lat, lng, format):
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
    data = _sendRequest(_defaultLat, _defaultLng, format)
    response = {
        'temp': data['main']['temp'],
        'windSpeed': data['wind']['speed'],
        'windDir': data['wind']['deg'],
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity']
    }
    return response


# returns temp
def getTemp(format='us'):
    data = _sendRequest(_defaultLat, _defaultLng, format)
    return data['main']['temp']


# returns wind speed
def getWindSpeed(format='us'):
    data = _sendRequest(_defaultLat, _defaultLng, format)
    return data['wind']['speed']


# returns wind direction
def getWindDir(format='us'):
    data = _sendRequest(_defaultLat, _defaultLng, format)
    return data['wind']['deg']


# returns pressure
def getPressure(format='us'):
    data = _sendRequest(_defaultLat, _defaultLng, format)
    return data['main']['pressure']


# returns humidity
def getHumidity(format='us'):
    data = _sendRequest(_defaultLat, _defaultLng, format)
    return data['main']['pressure']
