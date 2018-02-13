from django.urls import path, re_path

from places import views

app_name = 'places'

urlpatterns = [
    path('', views.places_home, name='home'),
    path('create/', views.place_create, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.place_detail, name='detail'),
]
