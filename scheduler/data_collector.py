from apscheduler.schedulers.blocking import BlockingScheduler
from agents.weather_agent import analyze_destinations

scheduler = BlockingScheduler()

def collect_data():
    print("Collecting climate data...")
    analyze_destinations()

scheduler.add_job(collect_data, 'interval', hours=6)

scheduler.start()