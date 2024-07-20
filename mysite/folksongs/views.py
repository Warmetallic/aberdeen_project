from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .models import Song, SongImage
from .forms import SignUpForm, SongForm
from django.shortcuts import render, get_object_or_404

# Code for this page was adapted and inspired by the lectures from Dr Scharlau at the University of Aberdeen - in the 'Enterprise Software Development' module.


# Create your views here.
def home(request):
    songs = Song.objects.all()
    return render(request, 'home.html', {'songs': songs})


def song(request, id):
    song = get_object_or_404(Song, id=id)
    images = SongImage.objects.filter(song=song)
    # images = request.FILES.getlist('images')
    # for img in images:
    #     SongForm.objects.create(images=img)
    # images = Song.objects.all()
    # {'images': images}
    return render(request, 'song.html', {'song': song, 'images': images})

def song_add(request):
    if request.method=="POST":
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.created_date = timezone.now()
            song.save()
            song=form.instance
            # return render(request, 'song_add.html', {'form': form, 'song': song})
            return redirect('song', id=song.id)
    else:
        form = SongForm()
    return render(request, 'song_add.html', {'form': form})

# Code for signup was adapted and inspired by https://docs.djangoproject.com/en/3.2/ref/templates/language/.

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.customer.first_name = form.cleaned_data.get('first_name')
        user.customer.last_name = form.cleaned_data.get('last_name')
        user.customer.address = form.cleaned_data.get('address')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password= password)
        login(request, user)
        return redirect('/')
    return render(request, 'signup.html', {'form': form})


# Code for search was adapted and inspired by https://www.youtube.com/watch?v=AGtae4L5BbI&ab_channel=Codemy.com.

def search(request):
    if request.method == "POST":
        name = request.POST.get('name', False)
        volume = request.POST.get('volume', False)
        author = request.POST.get('author', False)
        songs = Song.objects.filter(songName__icontains=name)
        volumes = Song.objects.filter(songVolume__icontains=volume)
        authors = Song.objects.filter(songAuthor__icontains=author)
        songFilters = Song.objects.filter(songName__icontains=name, songVolume__icontains=volume, songAuthor__icontains=author)
        return render(request, 'search.html', {'name': name,'volume': volume,'author': author,'songs': songs,
            'volumes': volumes,'songFilters': songFilters})
    else:
        return render(request, 'search.html', {})


def map(request):
    return render(request, 'map.html', {})


def help(request):
    return render(request, 'help.html', {})

def handler404(request):
    return render(request, '404.html', {})