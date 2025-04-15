import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_jobs():
    url = "https://vacancymail.co.zw/jobs/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_listings = soup.find_all('a', class_='job-listing')

    job_titles = []
    companies = []
    descriptions = []
    locations = []
    expiry_dates = []

    for job in job_listings:
        try:
            job_title = job.find('h3', class_='job-listing-title').get_text(strip=True)
        except AttributeError:
            job_title = 'No job title found'

        try:
            company = job.find('h4', class_='job-listing-company').get_text(strip=True)
        except AttributeError:
            company = 'No company found'

        try:
            description = job.find('p', class_='job-listing-text').get_text(strip=True)
        except AttributeError:
            description = 'No description found'

        try:
            # Extract location from the <li> containing the location icon
            location_li = job.find('i', class_='icon-material-outline-location-on')
            location = location_li.parent.get_text(strip=True) if location_li else 'No location found'
        except AttributeError:
            location = 'No location found'

        try:
            # Extract expiry date from the <li> containing the expiry date icon
            expiry_icon = job.find('i', class_='icon-material-outline-access-time')
            expiry_li = expiry_icon.find_parent('li') if expiry_icon else None
            if expiry_li and 'Expires' in expiry_li.get_text():
                expiry_date = expiry_li.get_text(strip=True).replace('Expires', '').strip()
            else:
                expiry_date = 'No expiry date found'
        except AttributeError:
            expiry_date = 'No expiry date found'

        job_titles.append(job_title)
        companies.append(company)
        descriptions.append(description)
        locations.append(location)
        expiry_dates.append(expiry_date)

    df = pd.DataFrame({
        'Job Title': job_titles,
        'Company': companies,
        'Description': descriptions,
        'Location': locations,
        'Expiry Date': expiry_dates
    })

    df.to_csv('scraped_jobs.csv', index=False)
    print("Job data scraped successfully and saved to 'scraped_jobs.csv'")

scrape_jobs()
