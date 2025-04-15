Job Listing Web Scraper*


This project is a Python-based web scraper that extracts job listings from the website VacancyMail. It collects the job title, company, description, location, and expiry date for each job listing and saves the data to a CSV file.

Features*

Scrapes job listings from the specified URL.

Extracts key details: Job Title, Company, Description, Location, and Expiry Date.

Saves the extracted data into a CSV file (scraped_jobs.csv).

Requirements*

To run this project, you need the following Python libraries:

requests: For sending HTTP requests to the website.

beautifulsoup4: For parsing and extracting data from the HTML content.

pandas: For creating and saving the extracted data into a CSV file.

Install the required libraries
You can install the necessary libraries by running the following commands in your terminal or command prompt:

bash

Copy

Edit

pip install requests

pip install beautifulsoup4

pip install pandas

Usage

Clone or download the project.

Create a Python script file (e.g., web_scraper.py) and paste the provided code into it.

Run the script:

Open your terminal and run the script using Python:

bash
Copy
Edit
python web_scraper.py
The script will scrape job listings from VacancyMail and save the extracted data in a CSV file called scraped_jobs.csv.

Output
The scraper will save the extracted job data into a CSV file (scraped_jobs.csv) with the following columns:

Job Title

Company

Description

Location

Expiry Date

Sample output in the CSV:

Job Title	Company	Description	Location	Expiry Date
Graduate Intern - People & Culture	World Vision	World Vision Zimbabwe is seeking a passionate and ...	Bulawayo	19 Apr 2025
Gardener	No company found	Gardener wanted to start ASAP.	Kwekwe	No expiry
Troubleshooting
Permission Denied Error: If you encounter a permission error when saving the CSV, make sure you have the necessary write permissions in the directory where you're running the script. Alternatively, try running the script with elevated privileges (e.g., using sudo on Linux or macOS).

No Job Data Found: Ensure that the website's structure hasn't changed. The scraper is dependent on specific HTML structure, so if the website updates its layout, the scraping code may need to be adjusted.

License
This project is licensed under the MIT License - see the LICENSE file for details.
