import json 
from services.weather_service import get_weather
from datetime import datetime

def analyse_destination():
    """Analyze weather for all destinations and store history."""
    with open("data/destinations.json") as f:
        destinations = json.load(f)
    
    results = []
    
    # Collect weather data for all destinations
    for place in destinations:
        weather = get_weather(place["lat"], place["lon"])
        results.append({
            "city": place["city"],
            "country": place["country"],
            "temperature": weather["temperature"],
            "humidity": weather["humidity"],
            "condition": weather["weather"]
        })
    
    # Store weather history after collecting all data
    with open("data/weather_history.json", "a") as f:
        record = {
            "timestamp": str(datetime.utcnow()),
            "data": results
        }
        json.dump(record, f)
        f.write("\n")
    
    return results