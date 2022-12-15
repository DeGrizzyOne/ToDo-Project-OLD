from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    register_Form = UserCreationForm()
    return render(request, 'ToDoListe/login.html', {'registerForm': register_Form,})

