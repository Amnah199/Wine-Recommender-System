from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape_wines(url, output):
    """
    Scrape wines from https://www.divino.de
    :param url: Full URL after choosing desired filters and choosing the number of elements per page e.g. https://www.divino.de/wein-aus-deutschland?sPage=1&sPerPage=48 OR https://www.divino.de/weisswein?p=1&n=12
    :param output: Absolute path where the data will be saved as XLSX file e.g. C:/Users/user/Desktop/wines.xlsx
    :return:
    """
    headers = ['Name', 'Beschreibung']
    data = []
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')

    page_to_parent_elem = soup.find('div', {"class": "display_sites"})

    page_to = 1
    if page_to_parent_elem:
        page_to_elem = page_to_parent_elem.findAll('strong')
        if (page_to_elem):
            page_to = page_to_elem[1].text

    for i in range(1, int(page_to) + 1):
        if i != 1:
            if 'Page=' in url:
                req = requests.get(url.replace(f'Page=1', f'Page={i}', 1))
            else:
                req = requests.get(url.replace(f'p=1', f'p={i}', 1))
            soup = BeautifulSoup(req.text, 'lxml')

        wines = soup.find_all('div', {"class": "divinoArtbox"})
        for wine in wines:
            url_details = wine.find('a')['href']
            details = requests.get(url_details)
            soup = BeautifulSoup(details.text, 'lxml')

            name_container = soup.find('div', attrs={"id": 'detailbox'})
            name = name_container.find('h1').text

            description_container = soup.find('div', attrs={"id": 'description'})
            description_parts = description_container.find_all('p')

            description = ''
            for desc_part in description_parts:
                if desc_part.text.startswith('Wichtige Informationen'):
                    break
                description = description + desc_part.text + ' '

            properties_container = soup.find('ul', {"class": "description_properties"})
            properties = properties_container.findAll('li')

            row_data = {'Name': name, 'Beschreibung': description}

            for prop in properties:
                prop_value = prop.findAll('span')

                header = prop_value[0].text

                if header not in headers:
                    headers.append(header)
                    headers.append(headers.pop(headers.index('Beschreibung')))

                row_data[header] = prop_value[1].text

            data.append(row_data)

    df = pd.DataFrame(data, columns=headers)
    df.to_excel(output, engine='xlsxwriter')