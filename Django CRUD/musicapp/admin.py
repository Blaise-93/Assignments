from django.contrib import admin
from .models import Lyric, Song, Artiste

admin.site.register(Artiste)
admin.site.register(Song)
admin.site.register(Lyric)
