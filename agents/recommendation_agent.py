# Recommendation agent implementation
from utils.scoring import compute_score
def recommend_places(weather_data):
    ranked = []
    for place in weather_data:
        score = compute_score(
            place["temperature"],
            place["humidity"]
        )
        place["score"] = score
        ranked.append(place)
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked[:5]