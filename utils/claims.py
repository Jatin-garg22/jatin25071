from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def extract_claims(text):

    prompt = f"""
    Extract factual claims containing:
    - numbers
    - dates
    - statistics
    - percentages
    - technical or financial facts

    Return ONLY valid JSON array.

    Example:
    [
      {{
        "claim": "India's GDP grew by 7% in 2024"
      }}
    ]

    Text:
    {text[:8000]}
    """

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content

    output = output.replace("```json", "").replace("```", "").strip()

    return json.loads(output)