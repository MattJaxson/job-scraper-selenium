# Job Scraper for Indeed

A Python-powered scraper that uses Selenium and `undetected_chromedriver` to bypass basic bot detection and grab job listings from Indeed.com. Currently focused on a single search query and location but can be expanded to multiple pages or queries.

---

## Features

- Uses `undetected_chromedriver` to reduce detection by Indeed.
- Randomized delays to mimic human browsing patterns.
- Extracts job title, company, location, salary, and job summary.
- Saves results to a CSV file.

---

## Requirements

- Python 3.8+
- Google Chrome installed
- ChromeDriver (managed automatically by `undetected_chromedriver`)

---

## Setup

1. **Clone the repo:**

```bash
git clone https://github.com/MattJaxson/job-scraper-selenium.git
cd job-scraper-selenium
```

2. **Create and activate a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
(If you don’t have a requirements.txt, install manually:)
```bash
pip install undetected-chromedriver pandas
```
Usage
Default run:
```bash
python3 jb_scraper_selenium.py
```
Tips:

You may see 0 jobs if Indeed detects a bot or captcha—running again or solving the captcha manually (by commenting out headless mode) usually helps.

Notes
Currently limited to 1 page to avoid detection.

Future plans could include:

Rotating user agents or proxies.

Command-line arguments for search terms and locations.

Integration with other job sources (Adzuna, LinkedIn).

Contributing
PRs welcome! Let’s build out the toolkit.

License
MIT License

