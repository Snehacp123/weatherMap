
import requests
from django.shortcuts import render
from django.http import HttpResponse

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"

def get_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def get_temperature_on_date(weather_data, target_date):
    for entry in weather_data["list"]:
        if entry['dt_txt'] == target_date:
            return entry['main']['temp']
    return None

def get_wind_speed_on_date(weather_data, target_date):
    for entry in weather_data["list"]:
        if entry['dt_txt'] == target_date:
            return entry['wind']['speed']
    return None

def get_pressure_on_date(weather_data, target_date):
    for entry in weather_data["list"]:
        if entry['dt_txt'] == target_date:
            return entry['main']['pressure']
    return None

def index(request):
    if request.method == "POST":
        city = request.POST.get("city")
        option = request.POST.get("option")
        
        weather_data = get_weather_data(city)

        if option == "1":
            target_date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature_on_date(weather_data, target_date)
            result = [("Temperature", temperature)] if temperature is not None else []
        elif option == "2":
            target_date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed_on_date(weather_data, target_date)
            result = [("Wind Speed", wind_speed)] if wind_speed is not None else []
        elif option == "3":
            target_date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure_on_date(weather_data, target_date)
            result = [("Pressure", pressure)] if pressure is not None else []
        else:
            result = []

        return render(request, 'index.html', {'result': result})

    return render(request, 'index.html')
