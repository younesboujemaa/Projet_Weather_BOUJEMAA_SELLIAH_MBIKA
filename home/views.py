from django.shortcuts import render
import urllib.request
import json


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        # print(city)
        api_url = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=5edc16f1174cd120eb4da069d7164883').read()
        api_url2 = json.loads(api_url)
        lat = api_url2["coord"]["lat"]
        lon = api_url2["coord"]["lon"]
        api_url5 = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/air_pollution?lat=' + str(lat) + "&lon=" + str(lon) + "&appid=5edc16f1174cd120eb4da069d7164883").read()
        api_url6 = json.loads(api_url5)

        data = {
            "country": city,
            "weather_description": api_url2['weather'][0]['description'],
            "weather_temperature": api_url2['main']['temp'],
            "weather_pressure": api_url2['main']['pressure'],
            "weather_humidity": api_url2['main']['humidity'],
            "weather_wind": api_url2['wind']['speed'],
            "weather_pollution": api_url6['list'][0]['main']['aqi'],
            "weather_icon": api_url2['weather'][0]['icon'],
        }

    else:
        city = None
        data = {
            "country": None,
            "weather_description": None,
            "weather_temperature": None,
            "weather_pressure": None,
            "weather_humidity": None,
            "weather_wind": None,
            "weather_pollution": None,
            "weather_icon": None,
        }
    print(data['weather_icon'])
    return render(request, 'home/index.html', {"city": city, "data": data})

