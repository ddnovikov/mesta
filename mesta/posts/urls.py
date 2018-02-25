from django.urls import path, re_path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.post_list, name='home'),
    path('search/', views.post_search, name='search'),
    path('create/', views.post_create, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/update/$', views.post_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', views.post_delete, name='delete'),
]
