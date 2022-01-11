from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view


@api_view(['GET'])
def search_wines(request, criteria=""):
    return HttpResponse("""
    {
    "wines":
     [
        {
            "id": 1,
            "name": "2017 Primitivo di Madura",
            "picture_url": "http://127.0.0.1:8080/testimage.png"
        },
        {
            "id": 5,
            "name": "Susumaniello 2020di Epicuro",
            "picture_url": "http://127.0.0.1:8080/testimage.png"
        }
    ]
    }""")


@api_view(['GET'])
def get_recommendations(request):
    return HttpResponse("""{
  "sellers": [
    {
      "rank": 1,
      "id": 1,
      "name": "Jacques",
      "info": [
        { "label": "address", "content": "Spiegelturm 2 48143 Münster" },
        { "label": "whatever", "content": "info we have on the wineseller" }
      ]
    },
    {
      "rank": 2,
      "id": 3,
      "name": "second seller",
      "info": [
        { "label": "address", "content": "Spiegelturm 2 48143 Münster" },
        { "label": "whatever", "content": "info we have on the wineseller" }
      ]
    },
    {
      "rank": 3,
      "id": 2,
      "name": "third seller",
      "info": [
        { "label": "address", "content": "Spiegelturm 2 48143 Münster" },
        { "label": "whatever", "content": "info we have on the wineseller" }
      ]
    }
  ],
  "wines": [
    { "rank": 1, "id": 1, "name": "abcd", "picture_url": "http://127.0.0.1:8080/testimage.png" },
    { "rank": 2, "id": 4, "name": "asdasd", "picture_url": "http://127.0.0.1:8080/testimage.png" },
    { "rank": 3, "id": 3, "name": "xcv", "picture_url": "http://127.0.0.1:8080/testimage.png" },
    { "rank": 4, "id": 2, "name": "xcvxvc", "picture_url": "http://127.0.0.1:8080/testimage.png" },
    { "rank": 5, "id": 5, "name": "xcvxvc", "picture_url": "http://127.0.0.1:8080/testimage.png" },
    { "rank": 6, "id": 6, "name": "xcvxvc", "picture_url": "http://127.0.0.1:8080/testimage.png" }
  ]
}
""")


@api_view(['GET'])
def get_profile(request):
    return HttpResponse("""{
  "wine_data": [
    {
      "selection_type": "multiselect",
      "name": "Type of Wine",
      "options": [
        { "option": "red", "selected": false },
        { "option": "white", "selected": true },
        { "option": "sparkling", "selected": false }
      ]
    },
    {
      "selection_type": "multiselect",
      "name": "Price",
      "options": [
        { "option": "under 10€", "selected": false },
        { "option": "10-20€", "selected": true },
        { "option": "over 20€", "selected": true }
      ]
    },
    {
      "selection_type": "search_field",
      "name": "Origin",
      "options": [
        { "option": "germany", "selected": true },
        { "option": "italy", "selected": true },
        { "option": "france", "selected": false }
      ]
    }
  ],
  "taste_data": [
    { "label": "tree fruit", "percentage": 0.2 },
    { "label": "red fruit", "percentage": 0.1 },
    { "label": "citrus fruit", "percentage": 0.5 },
    { "label": "cinnamon", "percentage": 0.3 }
  ]
}
""")


@api_view(['GET'])
def get_wine_details(request, id=0):
    return HttpResponse("""{
  "id": 1,
  "name": "abcd",
  "picture_url": "http://127.0.0.1:8080/testimage.png",
  "description": "lorem ipsum",
  "facts": [
    { "label": "region", "content": "italy, puglia" },
    { "label": "style", "content": "red" },
    { "label": "alc", "content": "12%" }
  ],
  "taste_data": [
    { "label": "tree fruit", "percentage": 0.2 },
    { "label": "red fruit", "percentage": 0.1 },
    { "label": "citrus fruit", "percentage": 0.5 },
    { "label": "cinnamon", "percentage": 0.3 }
  ]
}""")
