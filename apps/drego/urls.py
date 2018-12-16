from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index)
    url(r'^login$', views.login)
    url(r'^login-page$', views.login_page)
    url(r'^register$', views.register)
    url(r'^register_page$', views.register_page)
]
