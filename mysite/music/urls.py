from django.conf.urls import url
from . import views

urlpatterns = [

    #music homepage
    url(r'^$', views.index, name='index'),

    # /music/457/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

]


