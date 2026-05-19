import os
import requests
from jobspy import scrape_jobs

# This pulls your secret Discord link from GitHub safely
webhook_urls = [
    os.getenv("DISCORD_WEBHOOK_URL_1"),
    os.getenv("DISCORD_WEBHOOK_URL_2"),
]

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

print(f"Jobs found: {len(jobs)}")

header = {
    "content": "📢 **Happy Tuesday @everyone! I've pulled this week's latest internship opportunities. Please review the details and application links below:**"
}

for webhook_url in webhook_urls:
    if webhook_url and webhook_url.strip():
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
    for webhook_url in webhook_urls:
        if webhook_url and webhook_url.strip():
            requests.post(webhook_url, json=payload)
