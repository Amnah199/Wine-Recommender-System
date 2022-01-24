import json

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseServerError
from WineAPI.models import Wine
from WineAPI.models import FlavorWine
from WineAPI.models import WineDto
from WineAPI.models import WineDetailsFacts
from WineAPI.models import WineDetailsTasteData
from WineAPI.models import WineDetailsDto
from django.core import serializers
from json import JSONEncoder
from rest_framework.decorators import api_view

@api_view(['GET'])
def search_wines(request, criteria=""):
    """
    Searches for wines based on given criteria
    :param request: http request object
    :param criteria: string criteria used for searching
    :return: List of wines found based on criteria
    """
    try:
        wines = Wine.objects.all().filter(wine_name__contains=criteria)
        wines_list = list(wines)
        wines_result = '{ "wines": ['

        for i in range(len(wines_list)):
            wines_result = wines_result + (WineDto(wines_list[i].wine_id, wines_list[i].wine_name, '')).toJSON() + ','
            if i == 29:
                break

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
    return HttpResponse("""{
  sellers: [
    {
      rank: 1,
      id: 1,
      name: "Jacques",
      lat: "51.94",
      lon: "7.65",
      info: [
        { label: "address", content: "Spiegelturm 2 48143 Münster" },
        { label: "whatever", content: "info we have on the wineseller" },
      ],
      url: "http://www.google.de",
    },
    {
      rank: 2,
      id: 3,
      name: "second seller",
      lat: "51.95",
      lon: "7.66",
      info: [
        { label: "address", content: "Spiegelturm 2 48143 Münster" },
        { label: "whatever", content: "info we have on the wineseller" },
      ],
      url: "http://www.google.de",
    },
    {
      rank: 3,
      id: 2,
      name: "third seller",
      lat: "51.96",
      lon: "7.64",
      info: [
        { label: "address", content: "Spiegelturm 2 48143 Münster" },
        { label: "whatever", content: "info we have on the wineseller" },
      ],
      url: "http://www.google.de",
    },
  ],
  wines: [
    {
      rank: 1,
      id: 1,
      name: "abcd",
      picture_url: "http://127.0.0.1:8080/testimage.png",
    },
    {
      rank: 2,
      id: 4,
      name: "asdasd",
      picture_url: "http://127.0.0.1:8080/testimage.png",
    },
    {
      rank: 3,
      id: 3,
      name: "xcv",
      picture_url: "http://127.0.0.1:8080/testimage.png",
    },
    {
      rank: 4,
      id: 2,
      name: "xcvxvc",
      picture_url: "http://127.0.0.1:8080/testimage.png",
    },
    {
      rank: 5,
      id: 5,
      name: "xcvxvc",
      picture_url: "http://127.0.0.1:8080/testimage.png",
    },
    {
      rank: 6,
      id: 6,
      name: "xcvxvc",
      picture_url: "http://127.0.0.1:8080/testimage.png",
    },
  ],
}
""")


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
        wines = Wine.objects.filter(wine_id=wine_id)
        wine_flavor = FlavorWine.objects.filter(wine_id__in=wines.values('wine_id'))

    except:
        return HttpResponseServerError()

    return HttpResponse(
        serializers.serialize('json', wine_flavor, fields=('wine_id', 'flavor_group', 'flavor_count', 'flavor_id')))

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
        wines = Wine.objects.filter(wine_id=id)
        wine_flavor = FlavorWine.objects.filter(wine_id__in=wines.values('wine_id'))

        wine = list(wines)[0]

        taste_data = []
        facts = [{'label' : 'region', 'content': wine.wine_country}, {'label' : 'style', 'content': wine.wine_type}, {'label' : 'alc', 'content': wine.wine_alcohol}]

        wine_details_dto = {}
        wine_details_dto['id'] = wine.wine_id
        wine_details_dto['name'] = wine.wine_name
        wine_details_dto['description'] = ''
        wine_details_dto['picture_url'] = ''
        wine_details_dto['facts'] = facts
        wine_details_dto['taste_data'] = taste_data

        wine_details_dto = json.dumps(wine_details_dto)
    except BaseException as ex:
        return HttpResponseServerError()

    return HttpResponse(wine_details_dto)
