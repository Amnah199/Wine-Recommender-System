# from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from seleniumwire import webdriver
from seleniumwire.utils import decode
import re
import pandas as pd
import bs4

import time
import json

import config
import pathlib


def parseWebsite(html):
    soup = bs4.BeautifulSoup(html, features="html.parser")
    for elem in soup.findAll("script"):
        script = str(elem)
        if '{"vintage":' in script:

            line = script.splitlines()[3]

            if line[-1] == ";":
                line = line[:-1]

            jsonString = line[line.index('{"vintage"'):]
            return json.loads(jsonString)


chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=" + config.userAgent)
chrome_options.add_argument("--proxy-server=localhost:8899")
chrome_options.headless = True
chrome_prefs = {}
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_options.add_argument('lang=en')
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}


driver = webdriver.Chrome(options=chrome_options,
                          executable_path=config.chromedriver_path,
                          desired_capabilities=desired_capabilities)

driver.set_window_size(1920, 1080)

filePath = pathlib.Path(__file__).parent.resolve()


df = pd.read_csv(str(filePath)+"/../temp/wines_export.csv")

if not os.path.isdir(str(filePath) + "/../export"):
    os.mkdir(str(filePath) + "/../export")

for id, row in df.iterrows():
    link = "http://www.vivino.com" + row["link"]

    current_wine_dir_path = str(filePath) + "/../export/" + str(id) + "/"

    secondCondition = (os.path.isfile(current_wine_dir_path+"taste.json"))
    secondCondition = True

    if not(os.path.isfile(current_wine_dir_path+"vintage.json") and secondCondition):

        if not os.path.isdir(current_wine_dir_path):
            os.mkdir(current_wine_dir_path)

        def interceptor(request, response):
            global body
            global id

            if(re.match("http[s]?://www\.vivino\.com\/api\/wines\/.*\/tastes.*", request.url)):
                with open(current_wine_dir_path+"taste.json", "w") as taste_file:
                    pattern = re.compile("(?<=/wines\/)\d.*(?=\/tastes)|$")
                    id = re.findall(pattern, request.url)[0]
                    taste_data = json.loads(decode(response.body, response.headers.get(
                        'Content-Encoding', 'identity')))
                    taste_data["vivino_id"] = id
                    json.dump(taste_data, taste_file)

        driver.response_interceptor = interceptor
        driver.get(link)

        WebDriverWait(driver, config.timeout).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "vintage"))
        )
        with open(current_wine_dir_path+"vintage.json", "w") as vintage_file:
            json.dump(parseWebsite(driver.page_source), vintage_file)

        counter = 0

        while (counter < 2):
            try:
                WebDriverWait(driver, config.loadTime).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//div[contains(@class, 'tasteCharacteristics')] "))
                )

                break
            except:
                counter2 = 0
                while counter2 < 10:
                    try:

                        driver.execute_script("""window.scrollBy(0,400)""")
                        break
                    except:
                        print("error while scrolling")
                        time.sleep(1)
                        counter2 += 1
            counter += 1

        time.sleep(config.sleepTime)
