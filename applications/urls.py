from django.urls import path
from .views import *

urlpatterns = [
    path('apply_event/', apply_event, name='apply_event'),
]