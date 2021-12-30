import scrape_wines_wein_direktimport
import scrape_wines_divino

# Direkt-import:

# https://www.wein-direktimport.de/alle-weine/typ/weissweine/?p=1&o=1&n=96
# https://www.wein-direktimport.de/alle-weine/typ/rotweine/?p=1&o=1&n=96
# https://www.wein-direktimport.de/alle-weine/typ/roseweine/?p=1&o=1&n=96
# https://www.wein-direktimport.de/alle-weine/typ/schaumweine/?p=1&o=3&n=96 - sparkling
# https://www.wein-direktimport.de/alle-weine/typ/bioweine/?p=1&o=1&n=96 - bio
# https://www.wein-direktimport.de/alle-weine/typ/grosse-gewaechse/?p=1&o=1&n=96

scrape_wines_wein_direktimport.scrape_wines('https://www.wein-direktimport.de/alle-weine/typ/schaumweine/?p=1&o=3&n=96', 'C:/Users/zoran/Desktop/sparkling-di.xlsx')

# Divino:
# https://www.divino.de/blanquette-cremant?sPage=1&sPerPage=48
# https://www.divino.de/weisswein?sPage=1&sPerPage=48
# https://www.divino.de/rosewein?sPage=1&sPerPage=48
# https://www.divino.de/rotwein?p=1&n=48
# https://www.divino.de/dessertwein?sPage=1&sPerPage=48

#scrape_wines_divino.scrape_wines('https://www.divino.de/dessertwein?sPage=1&sPerPage=48', 'C:/Users/zoran/Desktop/dessert-divino.xlsx')