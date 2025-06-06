import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def indeed_job_scraper(search_query, location, num_pages=1, delay=1.5):
    base_url = 'https://www.indeed.com/jobs'
    jobs = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/117.0.0.0 Safari/537.36'
    }

    for page in range(num_pages):
        params = {
            'q': search_query,
            'l': location,
            'start': page * 10
        }
        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Failed to retrieve page {page+1}: Status code {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        job_cards = soup.find_all('div', class_='job_seen_beacon')

        for job_card in job_cards:
            title_elem = job_card.find('h2', class_='jobTitle')
            company_elem = job_card.find('span', class_='companyName')
            location_elem = job_card.find('div', class_='companyLocation')
            salary_elem = job_card.find('span', class_='salary-snippet')
            summary_elem = job_card.find('div', class_='job-snippet')

            job = {
                'title': title_elem.text.strip() if title_elem else None,
                'company': company_elem.text.strip() if company_elem else None,
                'location': location_elem.text.strip() if location_elem else None,
                'salary': salary_elem.text.strip() if salary_elem else None,
                'summary': summary_elem.text.strip().replace('\n', ' ') if summary_elem else None
            }
            jobs.append(job)

        time.sleep(delay)  # pause to avoid getting blocked

    return jobs

def save_to_csv(jobs, filename='matt_job_listings.csv'):
    df = pd.DataFrame(jobs)
    df.to_csv(filename, index=False)
    print(f'Saved {len(jobs)} jobs to {filename}')

if __name__ == '__main__':
    search_query = 'data scientist'
    location = 'Detroit, MI'
    jobs = indeed_job_scraper(search_query, location, num_pages=3, delay=1.5)
    save_to_csv(jobs)
