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
            "picture_url": "http://myurl.com"
        },
        {
            "id": 5,
            "name": "Susumaniello 2020di Epicuro",
            "picture_url": "http://myurl.com"
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
    { "rank": 1, "id": 1, "name": "abcd", "picture_url": "http://myurl.com" },
    { "rank": 2, "id": 4, "name": "asdasd", "picture_url": "http://myurl.com" },
    { "rank": 3, "id": 3, "name": "xcv", "picture_url": "http://myurl.com" },
    { "rank": 4, "id": 2, "name": "xcvxvc", "picture_url": "http://myurl.com" },
    { "rank": 5, "id": 5, "name": "xcvxvc", "picture_url": "http://myurl.com" },
    { "rank": 6, "id": 6, "name": "xcvxvc", "picture_url": "http://myurl.com" }
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
def get_wine_details(request, id = 0):
    return HttpResponse("""{
  "id": 1,
  "name": "abcd",
  "picture_url": "http://myurl.com",
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

@api_view(['GET'])
def get_swagger_config(request):
    return HttpResponse("""
    {
  "swagger": "2.0",
  "info": {
    "description": "Mock up design for WineRecommender",
    "version": "1.0.0",
    "title": "Swagger WineRecommender",
    "termsOfService": "http://swagger.io/terms/",
    "contact": {
      "email": "apiteam@swagger.io"
    },
    "license": {
      "name": "Apache 2.0",
      "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
    }
  },
  "host": "127.0.0.1:8000",
  "basePath": "/",
  "schemes": [
    "http"
  ],
  "paths": {
    "/WineAPI/search_wines/{search_content}": {
      "get": {
        "tags": [
          "WineAPI"
        ],
        "summary": "Returns wines based on search criteria",
        "description": "Returns wines based on search criteria",
        "operationId": "search_wines",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "search_content",
            "description": "Search criteria",
            "required": true,
            "type": "string",
            "format": "utf-8"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation"
          }
        }
      }
    },
    "/WineAPI/details/{id}": {
      "get": {
        "tags": [
          "WineAPI"
        ],
        "summary": "Returns wines based on search criteria",
        "description": "Returns wines based on search criteria",
        "operationId": "details",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "description": "Wine Id",
            "required": true,
            "type": "integer",
            "format": "int32"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation"
          }
        }
      }
    },
    "/WineAPI/recommendations/": {
      "get": {
        "tags": [
          "WineAPI"
        ],
        "summary": "Returns recommended wines",
        "description": "Returns recommended wines",
        "operationId": "recommendations",
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "successful operation"
          }
        }
      }
    },
    "/WineAPI/profile/": {
      "get": {
        "tags": [
          "WineAPI"
        ],
        "summary": "Returns wine profile for user",
        "description": "Returns wine profile for user",
        "operationId": "profile",
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "successful operation"
          }
        }
      }
    }
  },
  "externalDocs": {
    "description": "Find out more about Swagger",
    "url": "http://swagger.io"
  }
}
    """)