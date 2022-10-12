from django.urls import include
from django.urls import path

from .views import *
urlpatterns = [
   #path('', home, name='home'),
   path('', addFood, name='Add_Food'),
]