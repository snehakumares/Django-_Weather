import re
from django.shortcuts import render
import json
import urllib.request

def index(request):
    city = ''
    context = {}
    if request.method == 'POST':
        city = str(request.POST['city']).capitalize()
        api_key = <copy your api key here>
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key).read()
        json_data = json.loads(res)
        country_code = str(json_data['sys']['country'])
        latitude = str(json_data['coord']['lat'])
        longitude = str(json_data['coord']['lon'])
        weather = str(json_data['weather'][0]['description']).capitalize()
        temperature = str(json_data['main']['temp'])
        pressure = str(json_data['main']['pressure'])
        humidity = str(json_data['main']['humidity'])
        wind_speed = str(json_data['wind']['speed'])
        context = {
            'city': city,
            'country_code': country_code,
            'latitude': latitude,
            'longitude': longitude,
            'weather': weather,
            'temp': temperature,
            'pressure': pressure,
            'humidity': humidity,
            'windspeed': wind_speed
        }
    return render(request, 'index.html', context)
