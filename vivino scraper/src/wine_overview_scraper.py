import pathlib
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

filePath = pathlib.Path(__file__).parent.resolve()


# Setting up Chrome
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=" + config.userAgent)
chrome_options.headless = False
chrome_prefs = {}
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_options.experimental_options["prefs"] = chrome_prefs

driver = webdriver.Chrome(options=chrome_options,
                          executable_path=config.chromedriver_path)
driver.set_window_size(1920, 1080)

df = pd.DataFrame()

driver.get(config.link)
try:
    time.sleep(5)
    while True:
        time.sleep(config.sleepTime)

        element = WebDriverWait(driver, config.timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='explore-page-app']/div/div/div[2]/div[2]/div[1]/div[1]"))
        )

        html = element.get_attribute('outerHTML')
        attributes = BeautifulSoup(html, 'html.parser').a.attrs
        print(attributes["href"])

        df = df.append({"datetime": time.time(),
                        "link":  attributes["href"]}, ignore_index=True)
        driver.execute_script("""
            var results = document.getElementsByClassName("explorerPage__results--3wqLw")[0]
            results.children[0].removeChild(results.children[0].firstChild)
            """)


except Exception as err:
    print("Fehlermeldung:")
    print(err)
    traceback.print_exc()

df.drop_duplicates("link")
df.to_csv(str(filePath) + "/../temp/product_detail_links/"+config.link_file_name)
driver.close()
