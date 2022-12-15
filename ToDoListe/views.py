from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    register_Form = UserCreationForm()

    if request.method == 'POST':
        if request.POST["operator"] == "register":
            request.POST.pop("operator")
            register_Form = UserCreationForm(request.POST)
            if register_Form.is_valid():
                register_Form.save()


    return render(request, 'ToDoListe/login.html', {'registerForm': register_Form,})

