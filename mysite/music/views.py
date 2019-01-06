from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album': album})

def favourite(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (keyError, song.DoesNotExist):
        return render(request, 'music/details.html', {
            'album' : album,
            'error_message' : "You didn't select a valid song"
        })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album})

def favourite_songs(request):
    all_songs = Song.objects.all()
    return render(request, 'music/favourite.html', {'all_songs':all_songs})




