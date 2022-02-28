# Basic estimation
# Import vivino and local data

vivino['wine_year'].unique()
vivino['wine_year'] = vivino['wine_year'].replace("N.V.", np.NaN)
vivino['wine_year'] = vivino['wine_year'].fillna(0)
vivino['wine_year'] = pd.to_numeric(vivino['wine_year'].astype(int))
avg_year = (sum(vivino["wine_year"]) // len(vivino["wine_year"]))
vivino['wine_year'] = vivino['wine_year'].replace(0, 2009)
local['wine_year'].unique()
local['wine_year'] = local['wine_year'].replace(' Jahrgangscuvée ', np.NaN)
local['wine_year'] = local['wine_year'].replace(' 2017, plus vins de reserve ', 2017)
local['wine_year'] = local['wine_year'].replace(' 2016, plus vins de reserve ', 2016)
local["wine_year"] = local["wine_year"].replace(' 2017, 2018, 2019 ', 2018)
local["wine_year"] = local["wine_year"].replace(' 2014, 2015 ', 2015)
local['wine_year'] = local['wine_year'].fillna(0)
local['wine_year'] = pd.to_numeric(local['wine_year'].astype(int))
local['wine_year'] = local['wine_year'].fillna(2013)
local['wine_year'] = local['wine_year'].replace(0, 2013)
