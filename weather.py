import requests
from config import API_KEY

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"

FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_current_weather(city):
    params={
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(CURRENT_URL, params=params)
    return response.json()


def get_forecast(city):
    params={
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(FORECAST_URL, params=params)
    return response.json()