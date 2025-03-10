import requests
from django.shortcuts import render
from decouple import config

def get_weather_data(city):
    api_key = config('WEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def get_forecast_data(city):
    api_key = config('WEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def weather(request):
    city = request.GET.get('city', 'London')  # Default city is London
    weather_data = get_weather_data(city)
    forecast_data = get_forecast_data(city)

    context = {
        'city': city,
        'temperature': weather_data['main']['temp'],
        'humidity': weather_data['main']['humidity'],
        'wind_speed': weather_data['wind']['speed'],
        'description': weather_data['weather'][0]['description'],
        'icon': weather_data['weather'][0]['icon'],
        'forecast': forecast_data['list'][:5],  # Show 5-day forecast
    }
    return render(request, 'weather/weather.html', context)
