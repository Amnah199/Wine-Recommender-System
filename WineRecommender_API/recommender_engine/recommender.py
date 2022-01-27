
import numpy as np


def calcRecs(wines_list, user_profile, num_wines, structure_param = 0.5, tastes_param = 1, ratings_param = 1):
    user_profile["structure"] = np.array(user_profile["structure"].values())
    user_profile["tastes"] = np.array(user_profile["tastes"].values())
    for wine in wines_list:
        wine["wine_tastes"] = np.array(wine["wine_tastes"].values())
        wine["wine_structure"] = np.array(wine["wine_structure"].values())
        wine["wine_rating"] = wine["wine_rating"]/4
        wine["score"] = (structure_param * sum(user_profile["structure"]*wine["wine_structure"]) + tastes_param * sum(user_profile["tastes"]*wine["wine_tastes"])) * (ratings_param * wine["wine_rating"])
    
    wines_list = sorted(wines_list, key=lambda k: k["score"])
    return wines_list[:num_wines-1]

def generateProfile(wine_ids):
    
    return user_profile