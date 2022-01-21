# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:17:33 2022

@author: HP pc
"""

import pandas as pd
import json 
from sklearn.linear_model import LogisticRegression
import math


# fucntion to convert each taste vector to representation of 0 and 1
def one_hot_encoding(row):
    vector = [0] * len(all_tastes)
    for flavor in row["wine_tastes"]:
        try:
            i = all_tastes.index(flavor)
        except:
            i = all_tastes.index("Other")
        vector[i] = 1
    return vector

# function to assign label to the wine_type
def label_encoding(row):
    if (row["wine_type"] == "red"):
        return 0
    if(row["wine_type"] == "white"):
        return 1
    return None

def get_prediction(row):
    if (math.isnan(row["label"])):
        return clf.predict([row["features"]])
    return row["label"]


# function to decode label to wine type
def label_decoding(row):
    if (int(row["label"]) == 0):
        return "red"
    if(int(row["label"]) == 1):
        return "white"


## create a set of all tasting notes 
# with open("wine_data.json", mode="r", encoding="utf-8") as json_file:
#     wine_data = json.load(json_file)

# all_tastes = set()

# for k in wine_data:
#     all_tastes.update(k["wine_tastes"])
    

# print(all_tastes)

# # writing the data in json file for tastes
# data_file = open('all_tastes.json',mode="w", encoding="utf-8" )
# jsonString = json.dumps(list(all_tastes))

# data_file.write(jsonString)

# data_file.close()


## read generated taste file from above
with open("all_tastes.json", mode="r", encoding="utf-8") as json_file:
    all_tastes = json.load(json_file)    
all_tastes.sort()
all_tastes.append("Other") # append other to handle unidentified tastes 

## read wine_data
with open("wine_data.json", mode="r", encoding="utf-8") as json_file:
    wine_data = json.load(json_file)
   
    
## Data frame for wine_data 
df = pd.DataFrame(wine_data)
df["features"] = df.apply(one_hot_encoding, axis = 1)
df["label"] = df.apply(label_encoding, axis = 1)
print(df)


clf = LogisticRegression(random_state = 0, max_iter = 1000)
clf.fit(df[~df["label"].isna()]["features"].to_list(), df[~df["label"].isna()]["label"].to_list())


df["label"] = df.apply(get_prediction, axis = 1)


df["wine_type_imputed"] = df.apply(label_decoding, axis = 1)

## print(df["wine_type"].unique())
print (df[["wine_id", "wine_name", "wine_type","wine_type_imputed"]])
df1 = df[["wine_id", "wine_name","wine_type_imputed","wine_year","wine_alcohol","wine_country","wine_price"]]
 
    
## writing the data in json file 
data_file = open('imputed_wine_data.json', mode="w", encoding="utf-8" )
jsonString = df1.to_json(orient = 'records')



## jsonString = json.dumps(df_dict)

data_file.write(jsonString)

data_file.close()
count = 0

for k in df.index:
    if (df['wine_type'][k] != df['wine_type_imputed'][k]):
        count += 1
        ##print (testing_data['wine_name'][k])
print ("Total predictions:" , count)



