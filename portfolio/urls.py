from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^artwork$', views.artwork, name='Artwork'),
    url(r'^other', views.other, name='other'),
    url(r'^music$', views.music, name='Music'),
    url(r'^youtube$', views.youtube, name='Youtube'),
    url(r'^about$', views.about, name='About'),
    url(r'^gallery$', views.gallery, name='Gallery')
    
]