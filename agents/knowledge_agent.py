import json


def get_destination_info(city):

    with open("data/tourism_knowledge.json") as f:
        data = json.load(f)

    return data.get(city, "No information available.")