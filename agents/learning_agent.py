# Learning agent implementation
from openai import OpenAI

client = OpenAI()

def explain_recommendation(places):

    prompt = f"""
    Explain why these destinations are good for travel:

    {places}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content