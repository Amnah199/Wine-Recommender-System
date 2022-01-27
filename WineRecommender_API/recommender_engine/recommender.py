
import numpy as np


def calcRecs(wines_list, user_profile, num_wines = 10, structure_param = 0.5, tastes_param = 1, ratings_param = 1):
    user_structure = np.asarray(list(user_profile["structure"].values()))
    user_tastes = np.asarray(list(user_profile["tastes"].values()))

    for wine in wines_list:
        wine_tastes = np.asarray(list(wine["wine_tastes"].values()))
        wine_structure = np.asarray(list(wine["wine_structure"].values()))
        wine["score"] = (structure_param * np.sum(np.multiply(user_structure, wine_structure)) + tastes_param * np.sum(np.multiply(user_tastes, wine_tastes))) * (ratings_param * float(wine["wine_rating"])/4)
    
    wines_list = sorted(wines_list, key=lambda k: k["score"], reverse=True)

    if num_wines > len(wines_list):
        num_wines = len(wines_list)

    return wines_list[:num_wines-1]


def generateProfile(wine_ids):

    return user_profile