from tavily import TavilyClient
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def verify_claim(claim):

    search = tavily.search(query=claim, max_results=3)

    evidence = ""

    for result in search["results"]:
        evidence += f"""
        Title: {result['title']}
        Content: {result['content']}
        """

    prompt = f"""
    Claim:
    {claim}

    Evidence:
    {evidence}

    Decide whether the claim is:
    VERIFIED
    OUTDATED
    FALSE
    INSUFFICIENT DATA

    Also provide:
    - short explanation
    - corrected fact if needed

    Format:

    Verdict:
    Explanation:
    Correct Fact:
    """

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content