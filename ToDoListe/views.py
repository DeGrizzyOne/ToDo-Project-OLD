from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse

# Create your views here.

def index(request):
    return render(request, 'ToDoListe/login.html', {})

