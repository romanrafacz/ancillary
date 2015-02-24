from django.shortcuts import render
from django.http import HttpResponse

from register.forms import RegisterForm, EmailForm, PasswordForm

# Create your views here.

def index(request):
    return render(request, 'register/index.html', {})

def register(request):
    return render(request, 'register/register.html', {})

def newaccount(request):
    new_account= EmailForm()
    return render(request, 'register/newaccount.html', {'new_account':new_account})

def check_email(request):
    new_account= EmailForm()
    if request.method == "POST":
        email1 = request.POST['email']
        email2 = request.POST['confirm_email']
        if email1 == email2:
            account_form = RegisterForm()
            return render(request, 'register/userinfo.html', {'account_form': account_form})
        else:
            message = "emails do not match"
            return render(request, 'register/newaccount.html', {'new_account': new_account, 'message':message})

    account_form = RegisterForm()
    return render(request, 'register/userinfo.html', {'account_form': account_form})

def confirm_data(request):
    account_form = RegisterForm()
    return render(request, 'register/confirm_data.html', {'account_form': account_form})

def final_signup(request):
    password_form = PasswordForm()
    return render(request, 'register/final_signup.html', {'password_form':password_form})

def submit_form(request):
    return render(request, 'register/submit_form.html', {})
