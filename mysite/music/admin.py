from django.contrib import admin
from .models import Album, Song

#Registering Models

admin.site.register(Album)
admin.site.register(Song)