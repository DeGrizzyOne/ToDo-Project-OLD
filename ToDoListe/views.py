from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    register_Form = UserCreationForm()

    if request.method == 'POST':
        if request.POST["operator"] == "register":
            request_dict = request.POST.copy()
            request_dict.pop("operator")
            register_Form = UserCreationForm(request_dict)
            if register_Form.is_valid():
                register_Form.save()


    return render(request, 'mainpages/login.html', {'registerForm': register_Form,})

