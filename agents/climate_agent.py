import json
def analyze_climate():
    with open("data/weather_history.json") as f:

        records = f.readlines()

    print("Analyzing", len(records), "weather records")

    return len(records)
    