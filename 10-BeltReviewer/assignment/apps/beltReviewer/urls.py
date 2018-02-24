from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books$', views.books),
    url(r'^books/add$', views.add),
    url(r'^addbookreview$', views.addbookreview),
    url(r'^users/(?P<id>\d+)$', views.users),
]
