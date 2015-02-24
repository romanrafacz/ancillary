from django.shortcuts import render

from register.forms import RegisterForm

# Create your views here.

def index(request):
    return render(request, 'register/index.html', {})

def register(request):
    return render(request, 'register/register.html', {})

def newaccount(request):
    new_account = RegisterForm()
    return render(request, 'register/newaccount.html', {'new_account':new_account})
