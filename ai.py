from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


def analyze_jobs(jobs_data, role, years, current_role, skills):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found")

    client = genai.Client(
        api_key=api_key
    )

    print("Jobs received:", len(jobs_data))

    prompt = f"""
You are a career and job market analysis assistant.

Target role:
{role}

Experience:
{years} years

Current role:
{current_role}

Current skills:
{skills}

Job postings:
{jobs_data}

Analyze these job postings.

Provide:

1. Top matching jobs
2. Skills I already have
3. Skills I am missing
4. Skills I should prioritize learning
5. Resume improvements
6. Recommended projects
7. A practical transition plan

Keep the response concise and structured.
"""

    print("Sending job data to Gemini...")
    print("Prompt length:", len(prompt))

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    print("Gemini response received!")

    return response.text