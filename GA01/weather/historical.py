import requests

# Weather data format defaults to 'us', but can be optionally set as 'si' to use
# the International System of Units.

_forecastApiKey = '5e4981d279ea465087d2eec8584e9dcd'

# Lat and Long default to Ames, Iowa
_defaultLat = '42.0307810'
_defaultLng = '-93.6319130'

def _sendRequest(time,lat,lng, format):
    r = requests.get('https://api.forecast.io/forecast/'+_forecastApiKey+'/'+lat+','+lng+','+time+'?units='+format)
    data=r.json()
    return data

# returns all relevant data for specefied time
def getSnapshot(time,format='us'):
    data = _sendRequest(time,_defaultLat,_defaultLng,format)
    response = {
        'temp': data['currently']['temperature'],
        'windSpeed': data['currently']['windSpeed'],
        'windDir': data['currently']['windBearing'],
        'pressure': data['currently']['pressure'],
        'humidity': data['currently']['humidity']
    }
    return response

# returns temp for specefied time
def getTemp(time,format='us'):
    data = _sendRequest(time,_defaultLat,_defaultLng,format)
    return data['currently']['temperature']

# returns wind speed for specefied time
def getWindSpeed(time,format='us'):
    data = _sendRequest(time,_defaultLat,_defaultLng,format)
    return data['currently']['windSpeed']

# returns wind direction for specefied time
def getWindDir(time,format='us'):
    data = _sendRequest(time,_defaultLat,_defaultLng,format)
    return data['currently']['windBearing']

# returns pressure for specefied time
def getPressure(time,format='us'):
    data = _sendRequest(time,_defaultLat,_defaultLng,format)
    return data['currently']['pressure']

# returns humidity for specefied time
def getHumidity(time,format='us'):
    data = _sendRequest(time,_defaultLat,_defaultLng,format)
    return data['currently']['humidity']
