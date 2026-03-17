from apscheduler.schedulers.background import BackgroundScheduler
from agents.weather_agent import analyse_destination

scheduler = BackgroundScheduler()

def collect_weather():

    print("Agent collecting global climate data...")

    data = analyse_destination()

    print("Collected weather for", len(data), "destinations")


scheduler.add_job(
    collect_weather,
    "interval",
    hours=6
)

scheduler.start()