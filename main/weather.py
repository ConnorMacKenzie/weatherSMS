import json
import requests
import datetime


def getweather(lat, lon):
    url = ('https://api.darksky.net/forecast/'
           '421c7a52fa73fd39ec995a1e2c5ca9a1'
           '/' + str(lat) + ',' + str(lon))

    url2 = ('http://maps.googleapis.com/maps/api/geocode/json?'
            'latlng=' + str(lat) + ',' + str(lon))
    
    weather = requests.get(url)
    weatherData = json.loads(weather.text)

    location = requests.get(url2)
    locationData = json.loads(location.text)
    
    city = locationData['results'][0]['address_components'][3]['long_name']
    current = weatherData['currently']['summary']
    day = weatherData['hourly']['summary']
    temp = str(int(round((float(weatherData['currently']['temperature'])-32)*(5.0/9.0), 0)))

    report = ('Weather in ' + city + ' ' + str(datetime.date.today()) + ': \n \n'
              'Currently ' + temp + 'C and ' + current + '\n \n' +
              day)
    
    return report


