from django.urls import path

from places import views

app_name = 'places'

urlpatterns = [
    path('', views.places_home, name='places_home'),
]