from django.urls import path
from . import views

urlpatterns = [
    path('search_wines/<str:criteria>/', views.search_wines),
    path('profile/', views.get_profile),
    path('recommendations/', views.get_recommendations),
    path('details/<int:id>/', views.get_wine_details),
]