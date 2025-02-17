import os
import time
import pandas as pd
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import undetected_chromedriver as uc

# Load environment variables
load_dotenv()
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

# Random User-Agent to avoid detection
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
]
options = uc.ChromeOptions()
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = uc.Chrome(options=options)

# Open LinkedIn
driver.get("https://www.linkedin.com/login")
time.sleep(random.uniform(3, 6))  # Wait to avoid detection

# Open LinkedIn login page
driver.get("https://www.linkedin.com/login")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

# Fill in login credentials
driver.find_element(By.ID, "username").send_keys(EMAIL)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for login confirmation
time.sleep(random.uniform(5, 8))

# Check if login was successful
if "feed" in driver.current_url or "checkpoint" in driver.current_url:
    print("✅ Login successful")
else:
    print("❌ Login failed. Check credentials or CAPTCHA.")
    driver.quit()
    exit()

# Job search parameters
search_terms = [
    "Fullstack Developer", "Python Developer", "Software Engineer",
    "Remote Software Engineer", "Backend Developer", "Frontend Developer",
    "Machine Learning Engineer", "Data Engineer", "DevOps Engineer"
]
location = "Remote"
jobs_list = []

for term in search_terms:
    print(f"\n🔎 Searching for: {term}...")
    
    search_url = f"https://www.linkedin.com/jobs/search?keywords={term.replace(' ', '%20')}&location={location}&f_TPR=r86400&position=1&pageNum=0"
    driver.get(search_url)
    
    # Wait for job listings to load
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "scaffold-layout__list-container")))
    except:
        print(f"❌ No job postings found for {term} (Page did not load correctly)")
        continue

    time.sleep(random.uniform(4, 7))  # Human-like wait before scrolling

    # Scroll to load more jobs dynamically
    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(3, 6))  # Simulate real scrolling time

    job_cards = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

    if not job_cards:
        print(f"⚠ No jobs found for {term} (Possible bot detection)")
        continue

    print(f"✅ Found {len(job_cards)} jobs for {term}")

    for job in job_cards[:10]:  # Extract first 10 jobs
        try:
            title_element = job.find_element(By.CLASS_NAME, "base-search-card__title")
            title = title_element.text.strip()

            job_link_element = job.find_element(By.TAG_NAME, "a")
            job_link = job_link_element.get_attribute("href")

            company_element = job.find_element(By.CLASS_NAME, "base-search-card__subtitle")
            company = company_element.text.strip()

            location_element = job.find_element(By.CLASS_NAME, "job-search-card__location")
            location = location_element.text.strip()

            salary = "Not Listed"
            experience = "Not Listed"

            job_data = {
                "Job Title": title,
                "Company": company,
                "Location": location,
                "Salary": salary,
                "Experience": experience,
                "Application Link": job_link
            }
            jobs_list.append(job_data)

            # Print job details in the console
            print(job_data)

            time.sleep(random.uniform(2, 5))  # Wait before scraping next job (mimics real browsing)

        except Exception as e:
            print(f"Error extracting job data: {e}")

# Save to Excel if jobs were found
if jobs_list:
    df = pd.DataFrame(jobs_list)
    df.to_excel("linkedin_jobs.xlsx", index=False)
    print("\n✅ Job data saved to linkedin_jobs.xlsx")
else:
    print("❌ No job data collected. Possible CAPTCHA issue.")

# Print job list for verification
print("\n📌 FINAL JOB LIST:")
for job in jobs_list:
    print(job)

# Close WebDriver

