from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pan$', views.pan),
    url(r'^mine$', views.mine),
    url(r'^fight$', views.fight),
    url(r'^gamble$', views.gamble),
    url(r'^reset$', views.reset),
    url(r'^', views.index),
]
