from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    #path('gallery/', gallery, name='gallery'),
    path('about/', about, name='about'),
    path('calendar/', calendar_view, name='calendar'),
    path('gallery/', gallery, name='gallery'),
    path('gallery/<int:pk>/', album_detail, name='album-detail'),
    #path('registration/', registration, name='registration'),
]