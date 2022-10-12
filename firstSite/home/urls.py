from django.urls import include
from django.urls import path
from . import views
urlpatterns = [
    path('', views.current_datetime, name='current_datetime'),
]