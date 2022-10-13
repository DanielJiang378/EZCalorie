from django.urls import include
from django.urls import path
from .views import *

urlpatterns = [
   path('', home, name='home'),
   path('add_food/', addFood, name='add_food'),
   path('delete_food/<str:pk>/', deleteFood, name='delete_food'),
]