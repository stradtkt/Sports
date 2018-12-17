from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^login-page$', views.login_page),
    url(r'^register$', views.register),
    url(r'^register_page$', views.register_page),
    url(r'^plans$', views.plans),
    url(r'^weeks$', views.weeks),
    url(r'^weeks/(?P<week_id>\d+)/games$', views.games),
    url(r'^weeks/(?P<week_id>\d+)/games/(?P<game_id>\d+)$', views.single_game),
]
