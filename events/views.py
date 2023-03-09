from django.shortcuts import render
from .models import Event

from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Album
#from .forms import RegistrationForm


def gallery(request):
    albums = Album.objects.all()
    context = {
        'albums': albums,
    }
    return render(request, 'gallery.html', context)

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    photos = album.album_photos.all()[:10]
    context = {
        'album': album,
        'photos': photos,
    }
    return render(request, 'album_detail.html', context)







# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def calendar_view(request):
    events = Event.objects.all()
    return render(request, 'calendar.html', {'events': events})
