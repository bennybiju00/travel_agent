from agents.weather_agent import analyse_destination
from agents.recommendation_agent import recommend_places
from agents.llm_reasoning_agent import explain_recommendations
from agents.knowledge_agent import get_destination_info


def run_travel_agent():

    weather_data = analyse_destination()

    recommendations = recommend_places(weather_data)

    enriched_data = []

    for place in recommendations:

        info = get_destination_info(place["city"])

        place["tourism_info"] = info

        enriched_data.append(place)

    explanation = explain_recommendations(enriched_data)

    return {
        "recommendations": enriched_data,
        "explanation": explanation
    }