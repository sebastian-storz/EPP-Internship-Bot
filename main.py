import os
import requests
from jobspy import scrape_jobs

# This pulls your secret Discord link from GitHub safely
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

# 1. Search for public Engineering internships
# This ensures any UC/CSU student can apply without Handshake issues
jobs = scrape_jobs(
    site_name=["linkedin", "indeed"],
    search_term="Engineering Internship",
    location="California",
    results_wanted=5,
    hours_old=168, # Pulls the last week of postings
)

# 2. Format and send to Discord
for index, row in jobs.iterrows():
    payload = {
        "embeds": [{
            "title": f"🚀 {row['title']}",
            "description": f"**Company:** {row['company']}\n**Location:** {row['location']}",
            "url": row['job_url'],
            "color": 16776960 # UCLA Gold
        }]
    }
    requests.post(webhook_url, json=payload)