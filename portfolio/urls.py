from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Artwork$', views.Artwork, name='Artwork'),
    url(r'^other', views.other, name='other')
    
]