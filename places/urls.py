from django.urls import path, re_path

from places import views

app_name = 'places'

urlpatterns = [
    path('', views.places_home, name='home'),
    path('list/', views.place_list, name='list'),
    path('create/<str:place_base_type>', views.place_create, name='create'),
    re_path(r'^(?P<slug>[\w-]+)$', views.place_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/update$', views.place_update, name='update'),
]
