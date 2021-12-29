# Functionality
This module is used to scrape vivino data from overview pages of vivino

# Usage
1. modify config.py. A sample configuration is provided. For info on configuration check the section config.
2. run wine_overview_scraper.py. Repeat for all 
3. run combine_links to create a shared wines_export.csv with all links
4. run wine_detail_page_scraper.py to scrape the vintage and taste data. 

The easiest way to test this is using the vscode debug configurations.

# Config
sleepTime: wait after every scraped element to avoid bot detection

loadTime: time after which an element is assumed to not be available

timeout: time after which the execution of the programm is cancelled because detail page is not available

userAgent: userAgent thats used to avoid bot detection

link: link to page thats scraped by wine_overview_scraper.py

link_file_name: file with links created by wine_overview_scraper.py

chromedriver_path: driver for selenium. For more info visit: https://chromedriver.chromium.org/getting-started
