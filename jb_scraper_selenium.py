import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd
import time
import random

def indeed_job_scraper(search_query, location, num_pages=1):
    options = uc.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--headless')  # Commented out for now to see CAPTCHA pages

    driver = uc.Chrome(options=options)

    jobs = []

    for page in range(num_pages):
        start = page * 10
        url = f'https://www.indeed.com/jobs?q={search_query}&l={location}&start={start}'
        driver.get(url)
        print(f"Scraping page {page + 1}: {url}")
        time.sleep(random.uniform(5, 10))  # Random delay to be more human-like

        job_cards = driver.find_elements(By.CLASS_NAME, 'job_seen_beacon')

        for job_card in job_cards:
            try:
                title = job_card.find_element(By.CSS_SELECTOR, 'h2.jobTitle').text
            except:
                title = None
            try:
                company = job_card.find_element(By.CLASS_NAME, 'companyName').text
            except:
                company = None
            try:
                location_elem = job_card.find_element(By.CLASS_NAME, 'companyLocation')
                location_text = location_elem.text
            except:
                location_text = None
            try:
                salary_elem = job_card.find_element(By.CLASS_NAME, 'salary-snippet')
                salary = salary_elem.text
            except:
                salary = None
            try:
                summary_elem = job_card.find_element(By.CLASS_NAME, 'job-snippet')
                summary = summary_elem.text.replace('\n', ' ')
            except:
                summary = None

            job = {
                'title': title,
                'company': company,
                'location': location_text,
                'salary': salary,
                'summary': summary
            }
            jobs.append(job)

    driver.quit()
    return jobs

def save_to_csv(jobs, filename='matt_job_listings.csv'):
    df = pd.DataFrame(jobs)
    df.to_csv(filename, index=False)
    print(f'Saved {len(jobs)} jobs to {filename}')

if __name__ == '__main__':
    search_query = 'data scientist'
    location = 'Detroit, MI'
    jobs = indeed_job_scraper(search_query, location, num_pages=1)  # Limit to 1 page for now
    save_to_csv(jobs)
