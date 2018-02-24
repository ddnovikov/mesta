from django.urls import path

from misc import views

app_name = 'about'

urlpatterns = [
    path('', views.about, name='home'),
]
