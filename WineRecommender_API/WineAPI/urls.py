from django.urls import path
from . import views

urlpatterns = [
    path('getWines/', views.getWines),
]