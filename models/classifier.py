from groq import Groq
import os
from utils.env_loader import *

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def classify_query(query):
    messages = [
        {"role": "system", "content": "Classify the query as either 'troubleshooting' or 'provider_info'. Respond with ONLY one word."},
        {"role": "user", "content": query}
    ]
    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",
        messages=messages,
        temperature=0.0
    )
    return response.choices[0].message.content.strip().lower()