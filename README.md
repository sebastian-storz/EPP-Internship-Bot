[README.md](https://github.com/user-attachments/files/27748504/README.md)
# EPP Internship Bot 

An automated internship posting bot for the **Engineering Pathways Program (EPP)** community. Every Tuesday, it scrapes LinkedIn for the latest engineering internships and posts them directly to Discord — no Handshake required, so students from any UC or CSU can access the opportunities.

---

## How It Works

1. A GitHub Actions workflow runs automatically every Tuesday at 9:00 AM PST
2. `main.py` scrapes LinkedIn for recent engineering internship postings in California
3. Each job is formatted into a Discord embed and posted to the server via webhook

---

## Tech Stack

- **Python 3.10**
- [`python-jobspy`](https://github.com/Bunsly/JobSpy) — scrapes LinkedIn job listings
- `requests` — sends data to Discord via webhook
- `pandas` — organizes scraped job data
- **GitHub Actions** — runs the script on a schedule automatically

---

## Project Structure

```
EPP-Internship-Bot/
├── main.py                        # Core scraping and posting logic
├── requirements.txt               # Python dependencies
└── .github/
    └── workflows/
        └── schedule.yml           # GitHub Actions workflow
```

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/sebastian-storz/EPP-Internship-Bot.git
cd EPP-Internship-Bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your Discord Webhook
- Go to your Discord server → Server Settings → Integrations → Webhooks
- Create a new webhook for the channel you want to post in
- Copy the webhook URL

### 4. Add GitHub Secrets
Go to your GitHub repo → Settings → Secrets and variables → Actions and add:

| Secret Name | Value |
|---|---|
| `DISCORD_WEBHOOK_URL_1` | First server's webhook URL |
| `DISCORD_WEBHOOK_URL_2` | Second server's webhook URL |

### 5. Trigger a test run
Go to the **Actions** tab on GitHub → Weekly Internship Post → **Run workflow**

---

## Configuration

All search settings are in `main.py`:

```python
jobs = scrape_jobs(
    site_name=["linkedin"],
    search_term="Engineering Internship Summer 2026",
    location="California",
    results_wanted=10,
    hours_old=168,       # Posts from the last 7 days
    job_type="internship",
)
```

The schedule is set in `.github/workflows/schedule.yml`:
```yaml
- cron: '0 16 * * 2'  # Every Tuesday at 9:00 AM PST
```

---

## Why This Exists

UCLA's Handshake platform restricts job links to UCLA students only. This bot pulls directly from LinkedIn so that all UC and CSU students** in the EPP community can access and apply to the same opportunities.

---

## Contributing

Pull requests welcome. To add a new job board, add it to the `site_name` list (jobspy supports `linkedin`, `indeed`, `glassdoor`, and `zip_recruiter`).
