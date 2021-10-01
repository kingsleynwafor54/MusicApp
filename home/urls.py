from django.conf.urls import url
from django.urls import path

from .import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail,name="details"),
]