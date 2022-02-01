
#author: stepski011

"""
Packages to be installed
import pip
pip.main(['install', 'beautifulsoup4'])
pip.main(['install', 'HTMLParser'])
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"}

# RED WINES

red_wine_urls = [
    'https://www.jacques.de/wein/23/rotwein/frankreich/',
    'https://www.jacques.de/wein/31/rotwein/italien/',
    'https://www.jacques.de/wein/13/rotwein/spanien/',
    'https://www.jacques.de/wein/15/rotwein/chile/',
    'https://www.jacques.de/wein/3954/rotwein/deutschland/',
    'https://www.jacques.de/wein/3952/rotwein/australien/',
    'https://www.jacques.de/wein/3956/rotwein/argentinien/',
    'https://www.jacques.de/wein/3953/rotwein/suedafrika/',
    'https://www.jacques.de/wein/3957/rotwein/usa/',
    'https://www.jacques.de/wein/3955/rotwein/oesterreich/',
    ]

red_origins = [
    'Frankreich',
    'Italien',
    'Spanien',
    'Chile',
    'Deutschland',
    'Australien',
    'Argentinien',
    'Südafrika',
    'USA',
    'Österreich'
    ]

all_req = []
all_names = []
all_price = []
all_descriptions = []
all_origins = []
all_strength = []
all_characteristics = []
all_types = []
all_urls = []
all_thumbs = []

counter = 0

for countryWine in red_wine_urls:
    print(f'\n Scrapping on page: {countryWine}\n')
   
    request_page = requests.get(countryWine, headers = headers)
    soup = BeautifulSoup(request_page.content, 'html.parser')
    total_wines = soup.find_all('div', attrs  = {'class':'col col33'})
    
    for wines in total_wines:
        
        price = wines.find('div', attrs = {'class' : 'Price'}).text.replace(" ", "")        
        div_names = wines.find('div', attrs = {'class' : "description"})
        
        url_specific_wine = div_names.find('a', {'href' : True})['href']
        all_urls.append(url_specific_wine)
               
        details = requests.get(url_specific_wine, headers = headers)
        soup2 = BeautifulSoup(details.content, 'html.parser')
        description = soup2.find('div', attrs = {'class':'row description'}).text
        specific_wine_info = soup2.find_all('div', attrs = {'class':'products-informations'})
        names = soup2.find('h1', attrs = {"class":"name"}).text
                
        div_thumb = soup2.find('div', attrs = {'class' : 'imageContainer'})
        thumbs = div_thumb.find('a', {'href' : True})['href']
        all_thumbs.append(thumbs)
    
        for rows in specific_wine_info:
            names_s = rows.find('h1', attrs = {"class":"name"})
            strength = rows.find('div', attrs = {'class':'colC'})
            characteristics = rows.find('div', attrs = {'itemprop':'color'})  
            
            all_characteristics.append(characteristics)
            all_strength.append(strength)
            
        all_names.append(names)
        all_price.append(price)
        all_descriptions.append(description)        
        all_origins.append(red_origins[counter])
        all_types.append('Rotwein')
        
    counter += 1
    
    
# WHITE WINES

white_wine_urls = [
    'https://www.jacques.de/wein/3/weisswein/frankreich/',
    'https://www.jacques.de/wein/32/weisswein/italien/',
    'https://www.jacques.de/wein/3962/weisswein/spanien/',
    'https://www.jacques.de/wein/3966/weisswein/chile/',
    'https://www.jacques.de/wein/12/weisswein/deutschland/',
    'https://www.jacques.de/wein/3964/weisswein/australien/',
    'https://www.jacques.de/wein/3965/weisswein/oesterreich/',
    ]

white_origins = [
    'Frankreich',
    'Italien',
    'Spanien',
    'Chile',
    'Deutschland',
    'Australien',
    'Österreich'
    ]

counter = 0

for countryWine in white_wine_urls:
    print(f'\n Scrapping at page: {countryWine}\n')
   
    request_page = requests.get(countryWine, headers = headers)
    soup = BeautifulSoup(request_page.content, 'html.parser')
    total_wines = soup.find_all('div', attrs  = {'class':'col col33'})
    
    for wines in total_wines:
        
        price = wines.find('div', attrs = {'class' : 'Price'}).text.replace(" ", "")        
        div_names = wines.find('div', attrs = {'class' : "description"})
        
        url_specific_wine = div_names.find('a', {'href' : True})['href']
        all_urls.append(url_specific_wine)
       
        details = requests.get(url_specific_wine, headers = headers)
        soup2 = BeautifulSoup(details.content, 'html.parser')
        description = soup2.find('div', attrs = {'class':'row description'}).text
        specific_wine_info = soup2.find_all('div', attrs = {'class':'products-informations'})
        names = soup2.find('h1', attrs = {"class":"name"}).text     

        div_thumb = soup2.find('div', attrs = {'class' : 'imageContainer'})
        thumbs = div_thumb.find('a', {'href' : True})['href']
        all_thumbs.append(thumbs)            
        
        for rows in specific_wine_info:
            strength = rows.find('div', attrs = {'class':'colC'})
            characteristics = rows.find('div', attrs = {'itemprop':'color'})            
            all_characteristics.append(characteristics)
            all_strength.append(strength)
        
        all_names.append(names)
        all_price.append(price)
        all_descriptions.append(description)        
        all_origins.append(white_origins[counter])
        all_types.append('Weißwein')
        
    counter += 1
    
    
data = list(zip(all_names, all_types, all_price, all_descriptions, all_strength, all_characteristics, all_origins, all_urls, all_thumbs))
jacques_data_frame = pd.DataFrame(data, columns = ['Name', 'Typ', 'Preis in euro', 'Beschreibung', 'Alkoholgehalt', 'Weinstil', 'Herkunft', 'URL', 'Thumb'])

# Location for output file
jacques_data_frame.to_csv('jacques.csv')
print("\n Dataset created. \n")
