
from django.shortcuts import render, redirect
from django.views import View
from .forms import AlbumForm, AlbumModelForm
from django.contrib import messages
from .models import Song, Artiste, Lyric

# Creating a website that encompasses CRUD + L  implementaion on the frontend of Arstiste


class navigation(View):
    template_name = 'album/navigation.html'


def musicapp_list(request):
    album = Artiste.objects.all()
    context = {
        'album': album
    }
    return render(request, 'musicapp/album_list.html', context)


def musicapp_detail(request, pk):
    album = Artiste.objects.get(id=pk)
    print(album)
    context = {
        "album": album
    }
    return render(request, "musicapp/album_detail.html", context)


def musicapp_create(request):
    form = AlbumModelForm()  # we reassign the data if not validated
    if request.method == 'POST':
        print('Receiving a post request')
        form = AlbumModelForm(request.POST)
        # we can check if form is valid
        if form.is_valid():
            form.save()
            return redirect('/musicapp')  # redirect us back to our homepage
    context = {
        'form': form
    }
    messages.info(
        request, "Welcome, kindly create your artiste choice in the field provided. Also select your songs/lyrics.")
    return render(request, 'musicapp/album_update.html', context)


def musicapp_update(request, pk):
    album = Artiste.objects.get(id=pk)
    form = AlbumModelForm(instance=album)
    if request.method == 'POST':
        form = AlbumModelForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('/musicapp')
    context = {
        'form': form,
        'artiste': album
    }
    messages.info(
        request, "Hi there, do you want to updated the artiste!")
    return render(request, 'musicapp/album_update.html', context)


def musicapp_delete(request, pk):
    album = Artiste.objects.get(id=pk)
    album.delete()
    messages.info(
        request, "You have successfully deleted your Artiste.Thank you!")
    return render(request, 'musicapp/album_delete.html')
