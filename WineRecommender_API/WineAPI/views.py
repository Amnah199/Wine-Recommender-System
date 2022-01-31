import json

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseServerError
from rest_framework.decorators import api_view

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
            wines_result = wines_result + (WineDto(wine.wine_id, wine.wine_name, wine.wine_thumb)).toJSON() + ','

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
    return HttpResponse()


@api_view(['GET'])
def get_profile(request, wine_id=0):
    """
    Gets wine profile specific for a user
    :param wine_id: Id of Wine
    :param request: http object
    :return: wine preferences profile
    """
    if wine_id == 0:
        return HttpResponseBadRequest("Wine id must not be null or 0")

    try:
        wines = list(LocalWine.objects.filter(wine_id__in=wine_id))
        wine_flavors = list(FlavorWineGroup.objects.all().filter(wine_id__in=wines['wine_id']))
        wine_flavor_groups = list(FlavorGroup.objects.all())

        wine_count = len(wines)
        taste_data = {}
        for i in range(len(wine_flavor_groups)):
            taste_data[wine_flavor_groups[i].group_name] += wine_flavors[wine_flavor_groups[i].group_id].flavor_wine_group_score

        for i in range(len(wine_flavor_groups)):
            taste_data[wine_flavor_groups[i].group_name] = taste_data[wine_flavor_groups[i].group_name] / wine_count


    except:
        return HttpResponseServerError()

    return HttpResponse()


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

        wine_flavors = list(FlavorWineGroup.objects.all().filter(wine_id=wine.wine_id))
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
