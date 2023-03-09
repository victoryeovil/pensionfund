from django.shortcuts import render
from .models import Document
from django.http import HttpResponse

def document_list(request):
    documents = Document.objects.all()
    context = {
        'documents': documents
    }
    return render(request, 'document_list.html', context)




def document_download(request, document_id):
    document = Document.objects.get(id=document_id)
    response = HttpResponse(document.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response
