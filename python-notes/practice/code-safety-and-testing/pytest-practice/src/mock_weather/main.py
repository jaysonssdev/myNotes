import requests

def get_weather(city):
    response = requests.get(f"https://api.weather.com/v1/{city}") # you can't control this API, and you don't want your test to fail because this back end may someday fails
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Could not fetch weather data")