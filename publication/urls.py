from django.urls import path
from .views import document_list, document_download

urlpatterns = [
    path('document_list/', document_list, name='document_list'),
    path('<int:document_id>/download/', document_download, name='document_download'),
]
