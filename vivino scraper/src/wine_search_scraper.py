import pathlib
from signal import SIG_DFL
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import traceback


from bs4 import BeautifulSoup
import time
import config
import pandas as pd
import json
import os
filePath = pathlib.Path(__file__).parent.resolve()


# Setting up Chrome
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=" + config.userAgent)
chrome_options.headless = True
chrome_prefs = {}
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_options.experimental_options["prefs"] = chrome_prefs

driver = webdriver.Chrome(options=chrome_options,
                          executable_path=config.chromedriver_path)
driver.set_window_size(1920, 1080)

df = pd.DataFrame()
if os.path.isfile(str(filePath) + "/../temp/product_detail_links/"+"missing_wines.csv"):
    df = pd.read_csv(
        str(filePath) + "/../temp/product_detail_links/"+"missing_wines.csv", index_col=False)


with open(str(filePath)+"/../search.json", "r") as file:
    json_file = json.load(file)
    n = 0
    n_len = len(json_file)
    for line in json_file:
        n += 1
        print(n, "/", n_len)
        try:
            nId = int(line["local_id"])
            dfId = df.local_id

            if(not dfId.isin([nId]).any()):
                queryString = line["search_string"]
                driver.get("https://www.vivino.com/search/wines?q=" +
                           str(queryString))

                element = WebDriverWait(driver, config.timeout).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//div[@class="search-results-list"]'))
                )
                html = element.get_attribute('innerHTML')
                attributes = BeautifulSoup(
                    html, 'html.parser').find_all('a', href=True)

                i = 0
                for attr in attributes:

                    link = attr["href"]

                    if "/wines/" in link:
                        i += 1
                        if i <= 3:
                            df = df.append({"datetime": time.time(),
                                            "link":  link, "local_id": line["local_id"]}, ignore_index=True)
                time.sleep(5)
        except Exception as err:
            print("Fehlermeldung:")
            print(err)
            traceback.print_exc()


df.drop_duplicates("link")
df.to_csv(str(filePath) + "/../temp/product_detail_links/" +
          "missing_wines.csv", index_label="scrape_id")
print("file saved")
driver.close()
