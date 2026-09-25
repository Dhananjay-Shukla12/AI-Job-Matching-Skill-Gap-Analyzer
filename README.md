# AI Job Market & Skill Gap Analyzer

An AI-powered tool that analyzes real job postings and compares their requirements with a candidate's skills, experience, and target role.

I built this project to simplify job-market research. Instead of manually going through multiple job descriptions, the application collects relevant postings, uses AI to analyze them, and provides insights into required skills and areas for improvement.

## What It Does

- **Job Scraping:** Uses Playwright to collect job titles and descriptions from Naukri.
- **AI Analysis:** Uses the Google Gemini API to analyze job requirements.
- **Skill Gap Insights:** Identifies skills and requirements that may be missing from the candidate's current profile.
- **Recommendations:** Provides job, skill, and resume-related recommendations.
- **PDF Report:** Generates a downloadable analysis report through Streamlit.

## Tech Stack

**Python · Playwright · Streamlit · Google Gemini API · FPDF · python-dotenv**

## How It Works

```text
User Input
    ↓
Playwright → Naukri Job Listings
    ↓
Job Titles & Descriptions
    ↓
Google Gemini
    ↓
Job & Skill Analysis
    ↓
Recommendations
    ↓
PDF Report
```

## Run Locally

```bash
git clone <repository-url>
cd ai-job-market-skill-gap-analyzer

pip install -r requirements.txt
playwright install
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Then run:

```bash
streamlit run app.py
```

> **Note:** Keep `.env` and `naukri.json` out of version control by adding them to `.gitignore`.
