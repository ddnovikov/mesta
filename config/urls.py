"""mesta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import RedirectView

from mesta.helpers_and_misc import urls as misc_urls
from mesta.places import urls as places_urls
from mesta.posts import urls as blogs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include(misc_urls, namespace='about')),
    path('places/', include(places_urls, namespace='places')),
    path('blogs/', include(blogs_urls, namespace='blogs')),
    path('', RedirectView.as_view(pattern_name='places:home', permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
