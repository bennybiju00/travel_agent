import os
from google.genai import Client
from dotenv import load_dotenv

load_dotenv()

# create Gemini client
client = Client(api_key=os.getenv("GEMINI_API_KEY"))


def explain_recommendations(recommendations):

    prompt = f"""
    You are a travel climate expert.

    Explain why these destinations are good travel choices
    based on weather conditions.

    Destinations:
    {recommendations}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text