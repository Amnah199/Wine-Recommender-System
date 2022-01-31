import json

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseServerError
from django.db.models import Avg
from rest_framework.decorators import api_view
import ast

import recommender_engine.recommender
from .models import *
from recommender_engine import *
from django.db.models import Avg

wine_types = ['red', 'sparkling', 'white', 'rosé']
countries = list(Wine.objects.values('wine_country').distinct())

sellers = [{
    "rank": 1,
    "id": 1,
    "name": "Wein Direktimport Scholz GmbH",
    "info": [
        {"label": "address", "content": "Wolbecker Straße 302 48155 Münster"},
        {"label": "tel", "content": "0251 39729960"},
        {"label": "email", "content": "info@wein-direktimport.de"}
    ]
},
    {
    "rank": 2,
    "id": 2,
    "name": "divino Weinhandel Tobias Voigt",
    "info": [
        {"label": "address", "content": "Vogelrohrsheide 80 48167 Münster"},
        {"label": "tel", "content": "0251 62 79 184"},
        {"label": "email", "content": "info@divino.de"}
    ]
},
    {
    "rank": 3,
    "id": 3,
    "name": "Jacques",
    "info": [
        {"label": "address", "content": "Warendorfer Str. 22 48145 Münster-Mauritz"},
        {"label": "tel", "content": "0251/36384"},
        {"label": "email", "content": "mauritz@jacques.de"}]}]

template = {
    "wine_data": [
        {
            "selection_type": "multiselect",
            "name": "Type of Wine",
            "options": [
                {"option": "red", "selected": False},
                {"option": "white", "selected": False},
                {"option": "sparkling", "selected": False}
            ]
        },
        {
            "selection_type": "multiselect",
            "name": "Price",
            "options": [
                {"option": "under 10€", "selected": False},
                {"option": "10-20€", "selected": False},
                {"option": "over 20€", "selected": False}
            ]
        },
        {
            "selection_type": "search_field",
            "name": "Origin",
            "options": [
                {"option": "germany", "selected": False},
                {"option": "italy", "selected": False},
                {"option": "france", "selected": False}
            ]
        }
    ],
    "taste_data": [
        {"label": "tree fruit", "percentage": 0.2},
        {"label": "red fruit", "percentage": 0.1},
        {"label": "citrus fruit", "percentage": 0.5},
        {"label": "cinnamon", "percentage": 0.3}
    ]
}
keys_taste = ['black_fruit', 'citrus_fruit', 'dried_fruit', 'earth', 'floral', 'microbio', 'non_oak', 'oak',
              'red_fruit', 'spices', 'tree_fruit', 'tropical_fruit', 'vegetal']

keys_structure = ["acidity", "fizziness", "intensity", "sweetness", "tannin"]


x = LocalWine.objects.filter(lw_type='red').values_list('wine', flat=True)

for key in keys_taste:
    print(WineFlavor.objects.filter(wine_id__in=x).aggregate(Avg(key)))

# for key in keys_structure:
#    print(WineStructure.objects.filter(wine_id__in=x).aggregate(Avg('wine_'+key)))


@api_view(['GET'])
def search_wines(request, criteria=""):
    """
    Searches for wines based on given criteria
    :param request: http request object
    :param criteria: string criteria used for searching
    :return: List of wines found based on criteria
    """
    try:
        wines = Wine.objects.all().filter(wine_name__icontains=criteria)[:30]
        wines_list = list(wines)
        wines_result = '{ "wines": ['

        for wine in wines_list:
            winethumb = ''
            if wine.wine_thumb:
                winethumb = wine.wine_thumb[2:]
            wines_result = wines_result + \
                (WineDto(wine.wine_id, wine.wine_name, winethumb)).toJSON() + ','

        wines_result = wines_result + '] }'

    except BaseException as ex:
        return HttpResponseServerError(ex)

    return HttpResponse(wines_result)


@api_view(['GET'])
def get_recommendations(request, profile):
    """
    Gets wine-recommendations
    :param request: http request object
    :param profile: profile
    :return: list of wines recommended
    """

    user_profile = json.loads(profile)
    print(user_profile)

    user_profile = {
        "tastes": {
            "black_fruit": 0.5,
            "citrus_fruit": 0.5,
            "dried_fruit": 0.2,
            "earth": 0,
            "floral": 0,
            "microbio": 0,
            "non_oak": 0.7,
            "oak": 0.1,
            "red_fruit": 0.1,
            "spices": 0.9,
            "tree_fruit": 0.3,
            "tropical_fruit": 0,
            "vegetal": 0
        },
        "structure": {
            "acidity": 0.5,
            "fizziness": 0.4,
            "intensity": 0.6,
            "sweetness": 0.1,
        }
    }

    wines = []  # list(Wine.objects.filter(wine_id__in=wine_ids))
    wine_flavors = []
    wine_structure = list(WineStructure.objects.all().filter(
        wine_id__in=[w.wine_id for w in wines]))

    wines_for_recommender_engine = []

    for wine in wines:
        wine_flavors_current = list(
            filter(lambda x: (x.wine_id == wine.wine_id), wine_flavors))
        wine_tastes = {}
        wine_structure_obj = {}

        if wine_flavors_current:
            flavor_list = wine_flavors_current[:13]
            wine_tastes['black_fruit'] = flavor_list[0].flavor_wine_group_score
            wine_tastes['citrus_fruit'] = flavor_list[1].flavor_wine_group_score
            wine_tastes['dried_fruit'] = flavor_list[2].flavor_wine_group_score
            wine_tastes['earth'] = flavor_list[3].flavor_wine_group_score
            wine_tastes['floral'] = flavor_list[4].flavor_wine_group_score
            wine_tastes['microbio'] = flavor_list[5].flavor_wine_group_score
            wine_tastes['non_oak'] = flavor_list[6].flavor_wine_group_score
            wine_tastes['oak'] = flavor_list[7].flavor_wine_group_score
            wine_tastes['red_fruit'] = flavor_list[8].flavor_wine_group_score
            wine_tastes['spices'] = flavor_list[9].flavor_wine_group_score
            wine_tastes['tree_fruit'] = flavor_list[10].flavor_wine_group_score
            wine_tastes['tropical_fruit'] = flavor_list[11].flavor_wine_group_score
            wine_tastes['vegetal'] = flavor_list[12].flavor_wine_group_score
        else:
            wine_tastes['black_fruit'] = 0
            wine_tastes['citrus_fruit'] = 0
            wine_tastes['dried_fruit'] = 0
            wine_tastes['earth'] = 0
            wine_tastes['floral'] = 0
            wine_tastes['microbio'] = 0
            wine_tastes['non_oak'] = 0
            wine_tastes['oak'] = 0
            wine_tastes['red_fruit'] = 0
            wine_tastes['spices'] = 0
            wine_tastes['tree_fruit'] = 0
            wine_tastes['tropical_fruit'] = 0
            wine_tastes['vegetal'] = 0

        wine_structure_current = list(
            filter(lambda x: (x.wine_id == wine.wine_id), wine_structure))

        if wine_structure_current:
            wine_structure_obj['acidity'] = wine_structure_current[0].wine_acidity
            wine_structure_obj['fizziness'] = wine_structure_current[0].wine_fizziness
            wine_structure_obj['intensity'] = wine_structure_current[0].wine_intensity
            wine_structure_obj['sweetness'] = wine_structure_current[0].wine_sweetness

        wines_for_recommender_engine.append(
            {'wine_id': wine.wine_id, 'wine_tastes': wine_tastes, 'wine_structure': wine_structure_obj, 'wine_rating': wine.wine_rating})

    wines_recommendation_result = recommender_engine.recommender.calculate_recommendations(
        wines_for_recommender_engine, user_profile)

    local_wines = LocalWine.objects.all().filter(
        wine_id__in=[w['wine_id'] for w in wines_recommendation_result])

    wines_result = []
    for i in range(len(local_wines) - 1):
        wines_result.append({'rank': i + 1, 'name': local_wines[i].lw_name, 'type': local_wines[i].lw_type,
                             'picture_url': local_wines[i].lw_url, 'id': local_wines[i].lw_seller})

    json_result = '{' \
                  """  "sellers": [ 
    
      ]
    }
  ], """ + '"wines": ' + json.dumps(wines_result) + ' }'
    return HttpResponse(json_result)


@api_view(['GET'])
def get_profile(request, wine_ids=[]):
    """
    Gets wine profile specific for a user
    :param request: http object
    :param wine_ids: wineids
    :return: wine preferences profile
    """
    wine_ids = json.loads(wine_ids)
    print(wine_ids)
    if len(wine_ids) == 0:
        return HttpResponseBadRequest("Wine id must not be null or 0")

    try:
        wines = list(Wine.objects.filter(wine_id__in=wine_ids))

        if not wines:
            return HttpResponseBadRequest("No wines found for specified Ids")

        wine_flavors = WineFlavor.objects.all().filter(
            wine_id__in=[w.wine_id for w in wines])

        wine_flavors_averages = wine_flavors.aggregate(black_fruit=Avg('black_fruit'), citrus_fruit=Avg('citrus_fruit'), dried_fruit=Avg('dried_fruit'),
                                                       earth=Avg('earth'), floral=Avg('floral'), microbio=Avg('microbio'),
                                                       non_oak=Avg('non_oak'), oak=Avg('oak'), red_fruit=Avg('red_fruit'),
                                                       spices=Avg('spices'), tree_fruit=Avg('tree_fruit'), tropical_fruit=Avg('tropical_fruit'),
                                                       vegetal=Avg('vegetal'))

        taste_data = [
            {'label': 'black_fruit',
                'percentage': wine_flavors_averages['black_fruit']},
            {'label': 'citrus_fruit',
                'percentage': wine_flavors_averages['citrus_fruit']},
            {'label': 'dried_fruit',
                'percentage': wine_flavors_averages['dried_fruit']},
            {'label': 'earth', 'percentage': wine_flavors_averages['earth']},
            {'label': 'floral', 'percentage': wine_flavors_averages['floral']},
            {'label': 'microbio',
                'percentage': wine_flavors_averages['microbio']},
            {'label': 'non_oak',
                'percentage': wine_flavors_averages['non_oak']},
            {'label': 'oak', 'percentage': wine_flavors_averages['oak']},
            {'label': 'red_fruit',
                'percentage': wine_flavors_averages['red_fruit']},
            {'label': 'spices', 'percentage': wine_flavors_averages['spices']},
            {'label': 'tree_fruit',
                'percentage': wine_flavors_averages['tree_fruit']},
            {'label': 'tropical_fruit',
                'percentage': wine_flavors_averages['tropical_fruit']},
            {'label': 'vegetal',
                'percentage': wine_flavors_averages['vegetal']}
        ]

        wine_type_options = []
        wine_origin_options = []
        wine_price_options = []
        multi_select_type = {'selection_type': 'multiselect',
                             'name': 'Type of Wine', 'options': wine_type_options}
        multi_select_price = {'selection_type': 'multiselect',
                              'name': 'Price', 'options': wine_price_options}
        search_field_origin = {'selection_type': 'search_field',
                               'name': 'Origin', 'options': wine_origin_options}

        distinct_types = []
        distinct_prices = {'<10': False, '10-20': False, '>20': False}
        distinct_origin = []
        for wine in wines:
            if wine.wine_type not in distinct_types:
                distinct_types.append(wine.wine_type)
            if wine.wine_country.strip() not in distinct_origin:
                distinct_origin.append(wine.wine_country.strip())
            if wine.wine_price < 10:
                distinct_prices['<10'] = True
            if 10 <= wine.wine_price <= 20:
                distinct_prices['10-20'] = True
            if wine.wine_price > 20:
                distinct_prices['>20'] = True

        for wine_type in wine_types:
            wine_type_options.append({'option': wine_type, 'selected': False})

        for wine_country in countries:
            wine_origin_options.append(
                {'option': wine_country['wine_country'], 'selected': False})

        for w_type in distinct_types:
            for opt in wine_type_options:
                if opt['option'] == w_type:
                    opt['selected'] = True
        for w_origin in distinct_origin:
            for opt in wine_origin_options:
                if opt['option'] == w_origin:
                    opt['selected'] = True

        wine_price_options.append(
            {'option': 'under 10€', 'selected': distinct_prices['<10']})
        wine_price_options.append(
            {'option': '10-20€', 'selected': distinct_prices['10-20']})
        wine_price_options.append(
            {'option': 'over 20€', 'selected': distinct_prices['>20']})

        wine_structure_averages = WineStructure.objects.filter(wine_id__in=wine_ids).aggregate(wine_acidity=Avg('wine_acidity'), wine_fizziness=Avg('wine_fizziness'), wine_intensity=Avg('wine_intensity'),
                                                       wine_tannin=Avg('wine_tannin'), wine_sweetness=Avg('wine_sweetness'))

        # construct json result object
        result = '{ "wine_data": [' + json.dumps(multi_select_type) + ',' + json.dumps(
            multi_select_price) + ',' + json.dumps(search_field_origin) + '],'
        result += '"taste_data": ' + json.dumps(taste_data) + ', "structure_data": ' + json.dumps(wine_structure_averages) + ' }'
    except BaseException as ex:
        print(ex)
        return HttpResponseServerError(ex)

    return HttpResponse(result)


@api_view(['GET'])
def get_wine_details(request, id=0):
    """
    Gets details for a wine
    :param request: http request object
    :param id: id of the wine
    :return: details of specified wine
    """

    if id == 0:
        return HttpResponseBadRequest("Wine id must not be null or 0")

    try:
        wines_list = LocalWine.objects.filter(lw_id=id)

        wine = list(wines_list)[0]

        if wine is None:
            return HttpResponseBadRequest()

        wine_flavors = list(WineFlavor.objects.all().filter(wine_id=wine.wine_id))

        if len(wine_flavors) > 0:
            wine_flavors = wine_flavors[0]

        taste_data = [{'label': 'black_fruit', 'percentage': wine_flavors.black_fruit},
                      {'label': 'citrus_fruit',
                          'percentage': wine_flavors.citrus_fruit},
                      {'label': 'dried_fruit', 'percentage': wine_flavors.dried_fruit},
                      {'label': 'earth', 'percentage': wine_flavors.earth},
                      {'label': 'floral', 'percentage': wine_flavors.floral},
                      {'label': 'microbio', 'percentage': wine_flavors.microbio},
                      {'label': 'non_oak', 'percentage': wine_flavors.non_oak},
                      {'label': 'oak', 'percentage': wine_flavors.oak},
                      {'label': 'red_fruit', 'percentage': wine_flavors.red_fruit},
                      {'label': 'spices', 'percentage': wine_flavors.spices},
                      {'label': 'tree_fruit', 'percentage': wine_flavors.tree_fruit},
                      {'label': 'tropical_fruit',
                          'percentage': wine_flavors.tropical_fruit},
                      {'label': 'vegetal', 'percentage': wine_flavors.vegetal}]

        facts = [{'label': 'region', 'content': wine.lw_region},
                 {'label': 'style', 'content': wine.lw_type},
                 {'label': 'country', 'content': wine.lw_country},
                 {'label': 'price', 'content': wine.lw_price},
                 {'label': 'seller', 'content': wine.lw_seller},
                 {'label': 'year', 'content': wine.lw_year}]

        wine_details_dto = {'id': wine.lw_id, 'name': wine.lw_name, 'description': wine.lw_description, 'link': wine.lw_url, 'picture_url': wine.lw_thumb,
                            'facts': facts, 'taste_data': taste_data, }
        wine_details_dto = json.dumps(wine_details_dto)
    except BaseException as ex:
        print(ex)
        return HttpResponseServerError()

    return HttpResponse(wine_details_dto)
