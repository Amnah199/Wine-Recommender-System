import scrape_wines_wein_direktimport
import scrape_wines_divino

# Direkt-import:

# https://www.wein-direktimport.de/alle-weine/typ/weissweine/?p=1&o=1&n=96
# https://www.wein-direktimport.de/alle-weine/typ/rotweine/?p=1&o=1&n=96
# https://www.wein-direktimport.de/alle-weine/typ/roseweine/?p=1&o=1&n=96
# https://www.wein-direktimport.de/alle-weine/typ/schaumweine/?p=1&o=3&n=96 - sparkling
# https://www.wein-direktimport.de/alle-weine/typ/bioweine/?p=1&o=1&n=96 - bio
# https://www.wein-direktimport.de/alle-weine/typ/grosse-gewaechse/?p=1&o=1&n=96


headersDI = ["Name:", "Hersteller:", "Erzeugnis aus:", "Region:",	"Wein:", "Jahrgang:",	"Rebsorte:", "Qualität:", "Alkohol in %:", 	"Geschmack:",	"Allergene:", \
             "Trinktemperatur in °C:",	"Trinkempfehlung:",	"Dekantieren:",	"Verschluß:",	"Säure g/l:",	"Restzucker g/l:",	"Boden:",	"Essen:",	"Ausbauart:", \
             "Auszeichnungen:",	"Paßt zu:",	"Lage:",	"Herstellung:",	"Produkt aus biologischem Anbau:",	"Biokontrollstelle:",	"Diverses:",	"Zutaten:",	"Preis:",	"Image:",	"Details-URL:",	"Verkostungsnotiz:"]

scrape_wines_wein_direktimport.scrape_wines('https://www.wein-direktimport.de/alle-weine/typ/weissweine/?p=1&o=1&n=96', 'C:/Users/zoran/Desktop/white-di.xlsx', headersDI)
scrape_wines_wein_direktimport.scrape_wines('https://www.wein-direktimport.de/alle-weine/typ/rotweine/?p=1&o=1&n=96', 'C:/Users/zoran/Desktop/red-di.xlsx', headersDI)
scrape_wines_wein_direktimport.scrape_wines('https://www.wein-direktimport.de/alle-weine/typ/roseweine/?p=1&o=1&n=96', 'C:/Users/zoran/Desktop/rose-di.xlsx', headersDI)
scrape_wines_wein_direktimport.scrape_wines('https://www.wein-direktimport.de/alle-weine/typ/schaumweine/?p=1&o=3&n=96', 'C:/Users/zoran/Desktop/sparkling-di.xlsx', headersDI)
scrape_wines_wein_direktimport.scrape_wines('https://www.wein-direktimport.de/alle-weine/typ/bioweine/?p=1&o=1&n=96', 'C:/Users/zoran/Desktop/bio-di.xlsx', headersDI)
scrape_wines_wein_direktimport.scrape_wines('https://www.wein-direktimport.de/alle-weine/typ/grosse-gewaechse/?p=1&o=1&n=96', 'C:/Users/zoran/Desktop/big-plantations-di.xlsx', headersDI)

# Divino:
# https://www.divino.de/blanquette-cremant?sPage=1&sPerPage=48
# https://www.divino.de/weisswein?sPage=1&sPerPage=48
# https://www.divino.de/rosewein?sPage=1&sPerPage=48
# https://www.divino.de/rotwein?p=1&n=48
# https://www.divino.de/dessertwein?sPage=1&sPerPage=48

#headers = ["Name", "Jahrgang", "Rebsorte", "Weingut", "Produktbezeichnung", "Ort", "Passt gut zu", "Herkunftsland", "Anlass", "Größe des Winzers", "Winzer", "Region", "Herstellungsmethode", "Art", "Lagerfähigkeit", "Charakteristik", 'Preis', 'Image', 'Details-URL', "Beschreibung"]

#scrape_wines_divino.scrape_wines('https://www.divino.de/blanquette-cremant?sPage=1&sPerPage=48', 'C:/Users/zoran/Desktop/sparkling-divino.xlsx', headers)
#scrape_wines_divino.scrape_wines('https://www.divino.de/weisswein?sPage=1&sPerPage=48', 'C:/Users/zoran/Desktop/white-divino.xlsx', headers)
#scrape_wines_divino.scrape_wines('https://www.divino.de/rosewein?sPage=1&sPerPage=48', 'C:/Users/zoran/Desktop/rose-divino.xlsx', headers)
#scrape_wines_divino.scrape_wines('https://www.divino.de/rotwein?p=1&n=48', 'C:/Users/zoran/Desktop/red-divino.xlsx', headers)
#scrape_wines_divino.scrape_wines('https://www.divino.de/dessertwein?sPage=1&sPerPage=48', 'C:/Users/zoran/Desktop/dessert-divino.xlsx', headers)