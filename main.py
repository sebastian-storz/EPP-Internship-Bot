import os
import requests
from jobspy import scrape_jobs

# This pulls your secret Discord link from GitHub safely
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

# 1. Search for public Engineering internships
# This ensures any UC/CSU student can apply without Handshake issues
jobs = scrape_jobs(
    site_name=["linkedin"],
    search_term="Engineering Internship Summer 2026",
    location="California",
    results_wanted=10,
    hours_old=168, # Pulls the last week of postings
    job_type="internship",
)

header = {
    "content": "📢 **This week's Engineering Internships**"
}

requests.post(webhook_url, json=header)


# 2. Format and send to Discord
for index, row in jobs.iterrows():
    payload = {
        "embeds": [{
            "title": f"🚀 {row['title']}",
            "description": (
                f"**Company:** {row['company']}\n"
                f"**Location:** {row['location']}\n"
                f"**Posted:** {row['date_posted']}"
            ),
            "url": row['job_url'],
            "color": 16776960 # UCLA Gold
        }]
    }

    requests.post(webhook_url, json=payload)