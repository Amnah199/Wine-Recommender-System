import numpy as np
from WineAPI.models import *


def calculate_recommendations(wines_list, user_profile, num_wines=10, structure_param=0.5, tastes_param=1, ratings_param=1):
    user_structure = np.asarray(list(user_profile["structure"].values()))
    user_tastes = np.asarray(list(user_profile["tastes"].values()))

    for wine in wines_list:
        wine_tastes = np.asarray(list(wine["wine_tastes"].values()))
        wine_structure = np.asarray(list(wine["wine_structure"].values()))
        wine["score"] = (structure_param * np.sum(np.multiply(user_structure, wine_structure)) + tastes_param * np.sum(
            np.multiply(user_tastes, wine_tastes))) * (ratings_param * float(wine["wine_rating"]) / 4)

    wines_list = sorted(wines_list, key=lambda k: k["score"], reverse=True)

    if num_wines > len(wines_list):
        num_wines = len(wines_list)

    wines_list = wines_list[:num_wines - 1]

    return wines_list


profile_template = {
    "taste_data": {
        "black_fruit": 0,
        "citrus_fruit": 0,
        "dried_fruit": 0,
        "earth": 0,
        "floral": 0,
        "microbio": 0,
        "non_oak": 0,
        "oak": 0,
        "red_fruit": 0,
        "spices": 0,
        "tree_fruit": 0,
        "tropical_fruit": 0,
        "vegetal": 0
    },
    "structure_data": {
        "acidity": 0,
        "fizziness": 0,
        "intensity": 0,
        "sweetness": 0,
        "tannin": 0
    }
}


# assumes input to be a list of wines, as well as template to fill in


def generate_profile(wines, profile_template):
    keys_taste = ['black_fruit', 'citrus_fruit', 'dried_fruit', 'earth', 'floral', 'microbio', 'non_oak', 'oak',
                  'red_fruit', 'spices', 'tree_fruit', 'tropical_fruit', 'vegetal']
    keys_structure = ["acidity", "fizziness", "intensity", "sweetness", "tannin"]
    # types_all = ["red", "white", "sparkling", "rosé"]

    # average_taste = np.zeros(13)
    # average_structure = np.zeros(5)
    seen_high = False
    seen_medium = False
    seen_low = False
    origins = set()
    types = set()

    for wine in wines:
        # if wine.wine_country not in origins:
        #     origins.add(wine.region)
        # if wine.wine_type not in types:
        #     types.add(wine.wine_type)
        # if not seen_low and wine.price < 10:
        #     options[0]["selected"] = True
        # if not seen_medium and wine.price > 10 and wine.price < 20:
        #     options[1]["selected"] = True
        # if not seen_high and wine.price > 20:
        #     options[2]["selected"] = True

        for key in keys_taste:
            profile_template["taste_data"][key] = wine.wine_tastes[key]
        for key in keys_structure:
            profile_template["structure_data"][key] = wine.wine_structure[key]

    for key in keys_taste:
        profile_template["taste_data"][key] = profile_template["taste_data"][key] / len(wines)
    for key in keys_structure:
        profile_template["structure_data"][key] = profile_template["structure_data"][key] / len(wines)

    return profile_template, types, origins, (seen_low, seen_medium, seen_high)
