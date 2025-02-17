# Linkedin-job-scraper

This Python application scrapes job listings from LinkedIn based on given search terms (e.g., "Fullstack Developer", "Python Developer", "Software Engineer") and stores the results in an Excel file. It also opens each search in a new tab for manual viewing and keeps the browser open after scraping.

# Features
Scrapes LinkedIn for job listings using predefined search terms.
Automatically logs into LinkedIn using valid credentials.
Opens each job search in a new browser tab for easy manual viewing.
Scrolls through the job listings to load more results.
Collects job data including the job title, company, location, salary, and a link to the job listing.
Outputs job data to an Excel file (linkedin_jobs.xlsx).
Prints job data to the console for quick review.
Uses undetected Selenium to avoid detection by LinkedIn's anti-bot mechanisms.

# Prerequisites
Before running the script, ensure you have the following installed:

Python 3.8 or higher
pip (Python package installer)
# Dependencies
You will need to install the following Python packages:

undetected-chromedriver: A package to help bypass Selenium detection.
selenium: WebDriver for controlling the browser.
pandas: For data manipulation and saving job data into Excel format.
openpyxl: Required by pandas for Excel support.
# You can install all dependencies by running:

bash
Copy
Edit
pip install undetected-chromedriver selenium pandas openpyxl
Setup
1. Clone the Repository
First, clone the repository to your local machine using Git.

bash
Copy
Edit
git clone https://github.com/yourusername/linkedin-job-scraper.git
cd linkedin-job-scraper
2. Set Up Your LinkedIn Login
Update the email and password variables in the linkedin_job_scraper.py script with your LinkedIn login credentials:

python
Copy
Edit
EMAIL = "your_email_here@gmail.com"
PASSWORD = "your_password_here"
3. Configure Search Terms
Update the SEARCH_TERMS list with the job titles you're interested in scraping. For example:

python
Copy
Edit
SEARCH_TERMS = [
    "Fullstack Developer remote",
    "Python Developer remote",
    "Software Engineer remote"
]
Running the Script
1. Start the Script
After ensuring the necessary dependencies are installed and your login credentials are set, run the script with the following command:

bash
Copy
Edit
python linkedin_job_scraper.py
2. How It Works
The script will open LinkedIn's login page and log in using the provided credentials.
It will loop through the list of search terms, opening each job search in a new browser tab.
The script will scroll through the job listings and collect job data such as title, company, location, salary, and link.
After collecting the job data, it will print the list of jobs to the terminal and save the data to an Excel file named linkedin_jobs.xlsx.
The browser will remain open, allowing you to manually inspect the job listings.
Customization
Search Terms: Update the SEARCH_TERMS list to search for different job titles or remote work.
Excel Output: The script saves job listings to an Excel file. You can modify the output file name and format as needed.
Job Details: The script currently captures basic job details (title, company, location, salary, and link). You can modify the code to capture more details if necessary.
Error Handling
The script includes basic error handling:

If no job listings are found for a specific search term, it will print a message like:
❌ No job postings found for Fullstack Developer.
If any issues occur while scraping, the script will continue scraping the next job listings and will log the error encountered.
Troubleshooting
1. Browser Closing Automatically
If your browser closes automatically after scraping, ensure you are using the latest version of undetected-chromedriver. You can also ensure headless mode is disabled if you'd like to see the browser action during scraping.

2. CAPTCHA or Account Lock
If LinkedIn triggers CAPTCHA or locks your account:

Consider using manual login once and saving your session cookies to bypass CAPTCHA.
Use rotating proxies if scraping a large number of listings to avoid IP bans.
Contributing
Feel free to submit pull requests, report issues, or suggest features. If you encounter any bugs or have suggestions for improvements, please open an issue on GitHub.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to undetected-chromedriver for making Selenium-based scraping stealthier.
Selenium WebDriver for controlling the browser.
Pandas for handling data and exporting to Excel.
Example Output
After running the script, the following will be saved in linkedin_jobs.xlsx:

Title	Company	Location	Salary	Link
Fullstack Developer	Company XYZ	Remote	$90,000	https://linkedin.com/job/1
Python Developer	Tech Corp	Remote	$100,000	https://linkedin.com/job/2
Software Engineer	DevWorks Ltd	San Francisco	$120,000	https://linkedin.com/job/3
Additionally, the job data will be printed to the terminal for quick review.
