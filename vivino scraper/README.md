# Readme

## Functionality

This module is used to scrape vivino data from overview pages of vivino

## Requirements

In order to use this software following software has to be installed:

- Python 3.x (In testing 3.8 was used)
- all necessary pip packages:
    use pip install -r requirements
- Chrome with ChromeDriver (in testing Chrome 98 was used with ChromeDriver 98.0.4758.102)
    See [ChromeDriver Documentation](https://chromedriver.chromium.org/home) for more information
    The chromedriver file has to be copied to ./dependencies or the path has to be specified in the ./src/config/config.py

## Usage

1. modify the configs described below.
2. Start scraping. Refer to Config below for more details about configuration.
2.1 run wine_overview_scraper.py. Repeat for all overview pages that you want to scraper
2.2 run wine_search_scraper.py.
3. run combine_links to create a shared wines_export.csv with all links
4. run wine_detail_page_scraper.py to scrape the vintage and taste data.
5. The results are stored in ./export

The easiest way to test this is using the vscode debug configurations.

## Config

There are three config files which are all located in src/config.

- config.py is used as a general config file and used by all parts of the program
- wine_overview_config.py is used to configure the overview page scraper. This includes link to scrape and output file.
- wine_search_config.py is used to configure the wine search. This includes the output file.
There is also wine_search.json which is used to provide search terms and matched local ids to be scraped.

## Transforming Scraping Results
We have included our scraping results as vivino_raw.zip.
To transform the scraping results from individual folders to an easily loadable list of item dictionaries, the enclosed extraction.py needs to be run from the command line within the top level vivino_raw folder. Since scraping was done in multiple runs, multiple export folders with identical subfolder names were generated. To combat this, the script was modified accordingly to iterate over all subfolders of the meta-level folder.
The resulting output of the script is included as vivino_data.json.