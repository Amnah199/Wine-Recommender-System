from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseServerError
from WineAPI.models import Wine
from WineAPI.models import FlavorWine
from django.core import serializers

# Create your views here.
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
        wines = serializers.serialize('json', Wine.objects.all().filter(wine_name__contains=criteria), fields=(
        'wine_id', 'wine_name', 'wine_type', 'wine_year', 'wine_alcohol', 'wine_country', 'wine_price'))
    except:
        return HttpResponseServerError()

    return HttpResponse(wines)


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
        wine = serializers.serialize('json', Wine.objects.filter(wine_id=id), fields=(
        'wine_id', 'wine_name', 'wine_type', 'wine_year', 'wine_alcohol', 'wine_country', 'wine_price'))
    except:
        return HttpResponseServerError()

    return HttpResponse(wine)
