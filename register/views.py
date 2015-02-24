from django.shortcuts import render

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
    account_form = RegisterForm()
    return render(request, 'register/userinfo.html', {'account_form': account_form})

def confirm_data(request):
    account_form = RegisterForm()
    return render(request, 'register/confirm_data.html', {'account_form': account_form})

def final_signup(request):
    password_form = PasswordForm()
    return render(request, 'register/final_signup.html', {'password_form':password_form})
