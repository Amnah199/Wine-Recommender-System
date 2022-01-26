import numpy as np

wine1 = [{'group': 'tree_fruit', 'score': 4300, 'mentions': 43},
         {'group': 'earth', 'score': 3458, 'mentions': 35},
         {'group': 'citrus_fruit', 'score': 2100, 'mentions': 21}, {
    'group': 'vegetal', 'score': 600, 'mentions': 6},

    {'group': 'spices', 'score': 100, 'mentions': 1}, {
        'group': 'non_oak', 'score': 7, 'mentions': 0},
    {'group': 'oak', 'score': 35, 'mentions': 0}]


wine2 = [{'group': 'tree_fruit', 'score': 4300, 'mentions': 43},
         {'group': 'earth', 'score': 3458, 'mentions': 34},
         {'group': 'citrus_fruit', 'score': 2100, 'mentions': 56}, {
    'group': 'vegetal', 'score': 600, 'mentions': 6},
    {'group': 'floral', 'score': 300, 'mentions': 3},
    {'group': 'tropical_fruit', 'score': 366, 'mentions': 3},
    {'group': 'spices', 'score': 100, 'mentions': 1}, ]


def _search_for_group(struct, name):

    for elem in struct:
        if elem["group"] == name:
            return elem

    return {"group": elem["group"], "value": 0}


def get_wine_profile(data):
    max_mentions = 0

    # get highest mention count
    for elem in data:
        if elem["mentions"] > max_mentions:
            max_mentions = elem["mentions"]

    # compute normalized mention count
    return [{"group": elem["group"], "value": elem["mentions"]/max_mentions} for elem in data]


def get_profile(wine_profile_array):
    # compare
    taste_dict = {}

    for wine_profile in wine_profile_array:
        for group in wine_profile:
            if(group["group"] in taste_dict.keys()):
                taste_dict[group["group"]].append(group["value"])
            else:
                taste_dict[group["group"]] = [group["value"]]

    profile = [{"group": key, "value": np.max(
        taste_dict[key])} for key in taste_dict.keys()]

    return profile


def get_score(wine_profile, user_profile):

    return[{"group": taste["group"], "value": taste["value"]*_search_for_group(user_profile, taste["group"])["value"]} for taste in wine_profile]


userProfile = get_profile([get_wine_profile(wine1), get_wine_profile(wine2)])


print(get_score(get_wine_profile(wine1), userProfile))
