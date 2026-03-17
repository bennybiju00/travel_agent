# API main implementation
from fastapi import FastAPI
from agents.weather_agent import analyse_destination
from agents.recommendation_agent import recommend_places
from agents.orchestrator import run_travel_agent

app = FastAPI()

@app.get("/recommend")
def get_recommendations():
    return run_travel_agent()

@app.on_event("startup")
def start_scheduler():
    print("Starting climate monitoring agent...")
    try:
        from scheduler.weather_scheduler import scheduler
        from apscheduler.schedulers.base import STATE_RUNNING
        if scheduler.state != STATE_RUNNING:
            scheduler.start()
    except Exception as e:
        print(f"Scheduler error: {e}")