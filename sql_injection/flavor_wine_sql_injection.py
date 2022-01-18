import pandas as pd
from sqlalchemy import create_engine
import json
from sqlalchemy.types import Integer, Text, String, DateTime, Float, JSON


with open('flavor_wine_data.json', mode="r", encoding="utf-8") as json_file:
        flavor_wine_data = json.load(json_file)

with open('flavor.json', mode="r", encoding="utf-8") as json_file:
    flavor = json.load(json_file)


df1 = pd.DataFrame()
nameList = []
groupList = []
countList = []
idList = []
fidList =[]

for k in range(len(flavor_wine_data)):
    temp = flavor_wine_data[k]
    nameList.append(temp["flavor_name"])
    groupList.append(temp["flavor_group"])
    countList.append(temp["flavor_count"])
    idList.append(temp["wine_id"])
    for j in range(len(flavor)):
        temp2 = flavor[j]
        if(temp2["flavor_name"] == temp["flavor_name"]):
            fidList.append(temp2["flavor_id"])
            break

seq = list(range(len(flavor_wine_data)))
df1['flavor_wine_id'] = seq

df1.insert(1,'flavor_group', groupList, False)
df1.insert(2,'flavor_count', countList, False)
df1.insert(3,'wine_id', idList, False)
df1.insert(4,'flavor_id', fidList, False)

print(df1)


## Inserting the data in postgresql table
table_name = 'flavor_wine'
engine = create_engine("postgresql://postgres:portaladmin@localhost:5432/wine_db")

df1.to_sql(
    table_name,
    engine,
    if_exists='replace',
    index=False,
    chunksize=500,
    dtype={
        "flavor_wine_id": Integer,
        "flavor_group": Text,
        "flavor_count": Integer,
        "wine_id": Integer,
        "flavor_id": Integer
    }
)

