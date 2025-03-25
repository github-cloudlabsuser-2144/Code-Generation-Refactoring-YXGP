import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data):
    if data:
        city = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather.capitalize()}")
    else:
        print("Error: Unable to fetch weather data.")

if __name__ == "__main__":
    API_KEY = "6af1162c89e539825d80e6d6af57fa4b"
    CITY_NAME = "San Cristobal,VE"  # Updated city
    weather_data = get_weather(CITY_NAME, API_KEY)
    display_weather(weather_data)

#"lat":7.7756663,"lon":-72.2214154 and other
#https://api.openweathermap.org/data/2.5/weather?lat=7.7756663&lon=-72.2214154&appid=6af1162c89e539825d80e6d6af57fa4b