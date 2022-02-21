import pandas as pd
from sqlalchemy import create_engine

from sqlalchemy.types import Integer, Text, String, DateTime, Float, JSON

 
df = pd.read_json('D:/WWU Muenster/Semester 3/DI/Project Files/imputed_wine_data.json')

df.columns = [c.lower() for c in df.columns]

print(df)

table_name = 'wine'

engine = create_engine("postgresql://postgres:portaladmin@localhost:5432/wine_db")
  

df.to_sql(
    table_name,
    engine,
    if_exists='replace',
    index=False,
    chunksize=500,
    dtype={
        "wine_id": Integer,
        "wine_name": Text,
        "wine_imputed_type": Text,
        "wine_year": Integer,
        "wine_alcohol":  Float,
        "wine_country": Text,
        "wine_price": Float
    }
)


