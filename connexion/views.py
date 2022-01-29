from django.contrib.auth import login, authenticate,logout # import des fonctions login et authenticate
from django.shortcuts import render, redirect 
from django.conf import settings
import urllib.request
import json
from . import forms


def logout_user(request):
    
    logout(request)
    return redirect('login')

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                message = 'Identifiants invalides.'

    return render(
        request, 'connexion/login.html', context={'form': form, 'message': message})
    


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
            return render(request,'connexion/jsuiconnecter.html', {'user' :user})
    return render(request, 'connexion/signup.html', context={'form': form})


def utilisateur_page(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        unit = request.POST.get('ForC')

        if unit == 'C':
            api_url = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=5edc16f1174cd120eb4da069d7164883').read()
            api_url2 = json.loads(api_url)
        elif unit =='F':
            api_url = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperials&appid=5edc16f1174cd120eb4da069d7164883').read()
            api_url2 = json.loads(api_url)
        lat = api_url2["coord"]["lat"]
        lon = api_url2["coord"]["lon"]
        api_url5 = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/air_pollution?lat=' + str(lat) + "&lon=" + str(
                lon) + "&appid=5edc16f1174cd120eb4da069d7164883").read()
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
    return render(request, 'connexion/jsuiconnecter.html', {"city": city, "data": data})
    return render(request, 'connexion/jsuiconnecter.html')







