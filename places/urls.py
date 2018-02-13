from django.urls import path

from places import views

app_name = 'places'

urlpatterns = [
    path('', views.places_home, name='home'),
    path('create', views.place_create, name='create'),
]
