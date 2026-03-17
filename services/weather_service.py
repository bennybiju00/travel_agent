import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(lat, lon):
    """Fetch weather data from OpenWeather API."""
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check if API returned an error
        if "main" not in data:
            print(f"API Error: {data}")
            return {
                "temperature": None,
                "humidity": None,
                "weather": "unknown"
            }
        
        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["main"]
        }
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return {
            "temperature": None,
            "humidity": None,
            "weather": "error"
        }