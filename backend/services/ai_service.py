import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_interaction_data(user_input: str):
    prompt = f"""
    You are a strict data extraction system.

    Extract structured data from the following medical sales interaction.

    Return ONLY valid JSON. No explanation. No code. No extra text.

    Fields:
    - doctor_name
    - product
    - notes
    - follow_up
    - date

    Rules:
    - Always return JSON
    - If data missing, use null
    - Convert relative dates like "next Monday" into YYYY-MM-DD format

    Input:
    {user_input}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("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"))