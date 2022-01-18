#! /usr/bin/env python3

import json
import csv
import pandas
 
    
taste_path = []
vintage_path = []
dictList = []
myList = []
price = 0
rose = 0
red = 0
white = 0
sparkling = 0
others = 0
wine_name = "none"

# array of file locations for json files
for i in range(0, 9750):
    taste_path.append("/home/p/wines/data/" + str(i) + "/taste.json")  # change file path here
    vintage_path.append("/home/p/wines/data/" + str(i) + "/vintage.json") # change file path here

    
for k in range(0, 9750):
    
    if k == 6582:
        continue
    
    # Opening JSON file and loading the data into the variable data
    with open(vintage_path[k], mode="r", encoding="utf-8") as json_file:
        wine_data = json.load(json_file)
    with open(taste_path[k], mode="r", encoding="utf-8") as json_file:
        taste_data = json.load(json_file)
        
    
    # Extracting desired attributes from vintage.json 
    vintage_key = wine_data["vintage"]
    wine_id = vintage_key["id"]
    wine_name = vintage_key["name"]
    wine_facts = vintage_key["wine_facts"]
    if "alcohol" in wine_facts.keys():
        wine_alcohol = wine_facts['alcohol']
    else: 
        wine_alcohol = 0
    wine_year = vintage_key['year']
    location = vintage_key['wine']
    region = location['region']
    if region != None:
        wine_region = region['name']
        country = region['country']
        wine_country = country['name']
    
        
    # Extracting price from vintage.json 
    if 'price' in wine_data.keys():
        price_key = wine_data['price']
        if price_key != None:
            wine_price = price_key['amount']
            print("Count: " + str(price))
            price += 1
    else:
        wine_price = 0
        
        
    # Extracting wine type by searching keywords 
    
    if (' blanc ' in wine_name.lower() or ' chardonnay ' in wine_name.lower() 
        or ' gewürztraminer ' in wine_name.lower() or ' albariño ' in wine_name.lower() 
        or ' riesling ' in wine_name.lower() or ' blanco ' in wine_name.lower() or ' soave ' in wine_name.lower()
        or ' grauburgunder ' in wine_name.lower()):
        wine_type = "white"
        white += 1
        
        
    elif (' primitivo ' in wine_name.lower() or ' shiraz ' in wine_name.lower() 
          or ' cabernet ' in wine_name.lower() or ' syrah ' in wine_name.lower() or ' nebbiolo ' in wine_name.lower() 
          or ' barbaresco ' in wine_name.lower() or ' crianza ' in wine_name.lower() or ' merlot ' in wine_name.lower() 
          or ' giscours ' in wine_name.lower() or ' spätburgunder ' in wine_name.lower()):
        wine_type = "red"
        red += 1

    else:
        wine_type = "none"

    if wine_type == "none":
        wine_key = wine_data["wine"]
        if wine_key != None:
            style_key = wine_key["style"]
            if style_key != None and "description" in style_key.keys():
                wine_desc = style_key["description"]
    
            if wine_desc != None:
                if (' white ' in wine_desc.lower() ):
                    wine_type = "white"
                    white += 1
                    
                elif (' rose ' in wine_desc.lower() or ' rosé ' in wine_desc.lower()):
                    wine_type = "rose"
                    rose += 1
                    
                elif (' red ' in wine_desc.lower()):
                    wine_type = "red"
                    red += 1
                
                elif (' sparkling ' in wine_desc.lower()):
                    wine_type = "sparkling"
                    sparkling += 1
    
                else:
                    wine_type = "other"
                    others +=1
    
    # Extracting desired attributes from taste.json 
    taste = taste_data["tastes"]
    flavor = taste["flavor"]

    structure = taste["structure"]
    taste_list = []

    try:
        for g in flavor:
            stats = {}
            stats["group"] = g["group"]
            stats["score"] = g["stats"]["score"]
            stats["mentions"] = g["stats"]["mentions_count"]
            stats["keywords"] = []
            if "primary_keywords" in g.keys():
                primary_key = g["primary_keywords"]
                for key in primary_key:
                    stats["keywords"].append((key["name"], key["count"]))
            taste_list.append(stats)
    except:
        print('no flavor data present')
        taste_list = None



	
    wine_dict = {
        "wine_id" : k,
        "wine_name" : wine_name,
        "wine_alcohol" : wine_alcohol,
        "wine_type" : wine_type,
        "wine_year" : wine_year,
        "wine_country" : wine_country,
        "wine_region": wine_region,
        "wine_price" : wine_price,
        "wine_structure": structure,
        "wine_tastes": taste_list
        
    }
    dictList.append(wine_dict)
    
    

# writing the data in json file 
data_file = open('wine_data.json',mode="w", encoding="utf-8" )
jsonString = json.dumps(dictList)

data_file.write(jsonString)

data_file.close()

print ("WHITE count: " + str(white))
print ('RED count: ' + str(red))
print ("ROSE count: " + str(rose))
print ("Sparkling count: " + str(sparkling))
print ("Others count: " + str(others))


