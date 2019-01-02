from django.http import HttpResponse
from .models import Album, Song

def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        link = '/music/'+ str(album.id)+'/'
        html += "<a href='"+ str(link) +"'>"+ album.album_title +"<br></a>"
    return HttpResponse(html)

def detail(request, album_id):
    to_display = "<h2>You are Looking at Album: " + str(album_id) + "</h2>"
    return HttpResponse(to_display)
