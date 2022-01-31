import json

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseServerError
from rest_framework.decorators import api_view
import ast

import recommender_engine.recommender
from .models import *
from recommender_engine import *


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
            wines_result = wines_result + \
                (WineDto(wine.wine_id, wine.wine_name, wine.wine_thumb)).toJSON() + ','

        wines_result = wines_result + '] }'
    except BaseException as ex:
        return HttpResponseServerError()

    return HttpResponse(wines_result)


@api_view(['GET'])
def get_recommendations(request):
    """
    Gets wine-recommendations
    :param request: http request object
    :return: list of wines recommended
    """
    wine_ids = [1230065, 1171794, 18440]

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

    wines = list(Wine.objects.filter(wine_id__in=wine_ids))
    wine_flavors = list(FlavorWineGroup.objects.all().filter(
        wine_id__in=[w.wine_id for w in wines]))
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
                            'picture_url': local_wines[i].lw_url, 'seller_id': local_wines[i].lw_seller})

    json_result = '{' \
                  """  "sellers": [ 
    {
      "rank": 1,
      "id": 1,
      "name": "Wein Direktimport Scholz GmbH",
      "info": [
        { "label": "address", "content": "Wolbecker Straße 302 48155 Münster" },
        { "label": "tel", "content": "0251 39729960" },
        { "label": "email", "content": "info@wein-direktimport.de" }
      ]
    },
    {
      "rank": 2,
      "id": 2,
      "name": "divino Weinhandel Tobias Voigt",
      "info": [
        { "label": "address", "content": "Vogelrohrsheide 80 48167 Münster" },
        { "label": "tel", "content": "0251 62 79 184" },
        { "label": "email", "content": "info@divino.de" }
      ]
    },
    {
      "rank": 3,
      "id": 3,
      "name": "Jacques",
      "info": [
        { "label": "address", "content": "Warendorfer Str. 22 48145 Münster-Mauritz" },
        { "label": "tel", "content": "0251/36384" },
        { "label": "email", "content": "mauritz@jacques.de" }
      ]
    }
  ], """ + '"wines": [' + json.dumps(wines_result) + '] }'
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
    if len(wine_ids) == 0:
        return HttpResponseBadRequest("Wine id must not be null or 0")

    try:
        wines = list(LocalWine.objects.filter(lw_id__in=wine_ids))
        wine_flavors = list(FlavorWineGroup.objects.all().filter(
            wine_id__in=[w.wine_id for w in wines]))
        wine_flavor_groups = list(FlavorGroup.objects.all())

        wine_count = len(wines)
        taste_data = {
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
        }

        for i in range(len(wine_flavor_groups) - 1):
            for j in range(wine_count - 1):
                wine_flavor_group_name = wine_flavor_groups[i].group_name
                wine_flavor_group_id = wine_flavor_groups[i].group_id
                wine_flavors_current = list(
                    filter(lambda x: (x.wine_id == wines[j].wine_id), wine_flavors))

                if not wine_flavors_current:
                    continue

                wine_flavors_current_percentage = list(
                    filter(lambda y: (wine_flavor_group_id == y.group_id), wine_flavors_current))
                taste_data[wine_flavor_group_name] += wine_flavors_current_percentage[0].flavor_wine_group_score

        for i in range(len(wine_flavor_groups)):
            taste_data[wine_flavor_groups[i].group_name] = taste_data[wine_flavor_groups[i].group_name] / wine_count

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
            if wine.lw_type not in distinct_types:
                distinct_types.append(wine.lw_type)
            if wine.lw_country.strip() not in distinct_origin:
                distinct_origin.append(wine.lw_country)
            if wine.lw_price < 10:
                distinct_prices['<10'] = True
            if 10 <= wine.lw_price <= 20:
                distinct_prices['10-20'] = True
            if wine.lw_price > 20:
                distinct_prices['>20'] = True

        for w_type in distinct_types:
            wine_type_options.append({'option': w_type, 'selected': True})
        for w_origin in distinct_origin:
            wine_origin_options.append({'option': w_origin, 'selected': True})

        wine_price_options.append(
            {'option': 'under 10€', 'selected': distinct_prices['<10']})
        wine_price_options.append(
            {'option': '10-20€', 'selected': distinct_prices['10-20']})
        wine_price_options.append(
            {'option': 'over 20€', 'selected': distinct_prices['>20']})

        # construct json result object
        result = '{ "wine_data": [' + json.dumps(multi_select_type) + ',' + json.dumps(
            multi_select_price) + ',' + json.dumps(search_field_origin) + '],'
        result += '"taste_data": [' + json.dumps(taste_data) + '] }'
    except BaseException as ex:
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

        wine_flavors = list(
            FlavorWineGroup.objects.all().filter(wine_id=wine.wine_id))
        wine_flavor_groups = list(FlavorGroup.objects.all())

        taste_data = []
        for i in range(len(wine_flavor_groups)):
            taste_data.append({'label': wine_flavor_groups[i].group_name,
                               'percentage': wine_flavors[wine_flavor_groups[i].group_id].flavor_wine_group_score})

        facts = [{'label': 'region', 'content': wine.lw_region},
                 {'label': 'style', 'content': wine.lw_type},
                 {'label': 'country', 'content': wine.lw_country},
                 {'label': 'price', 'content': wine.lw_price},
                 {'label:': 'seller', 'content': wine.lw_seller},
                 {'label:': 'url', 'content': wine.lw_url},
                 {'label:': 'year', 'content': wine.lw_year}]

        wine_details_dto = {'id': wine.wine_id, 'name': wine.lw_name, 'description': wine.lw_description, 'picture_url': wine.lw_url,
                            'facts': facts, 'taste_data': taste_data}

        wine_details_dto = json.dumps(wine_details_dto)
    except BaseException as ex:
        return HttpResponseServerError()

    return HttpResponse(wine_details_dto)
