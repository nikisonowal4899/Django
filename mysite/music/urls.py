from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [

    #music homepage
    url(r'^$', views.index, name='index'),

    # /music/457/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/457/favourite/
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),

    #/music/favourite.html "viewing the favourite songs"
    url(r'^favourite_songs/$', views.favourite_songs, name='favourite_songs'),

    #music/all_songs "Viewing all Songs"
    url(r'^all_songs/$', views.all_songs, name='all_songs'),

]