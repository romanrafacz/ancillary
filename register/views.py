from django.shortcuts import render, redirect
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
    new_account= EmailForm(data=request.POST)
    if request.method == "POST" and new_account.is_valid():
        email1 = request.POST['email']
        email2 = request.POST['confirm_email']
        if email1 == email2:
            return redirect('/register/user_data')
        else:
            message = "emails do not match"
            return render(request, 'register/newaccount.html', {'new_account': new_account, 'message':message})
    return render(request, 'register/newaccount.html', {'new_account': new_account})

    #account_form = RegisterForm()
    #return render(request, 'register/userinfo.html', {'account_form': account_form})

def user_data(request):
    account_form = RegisterForm()
    return render(request, 'register/userinfo.html', {'account_form': account_form})

def confirm_data(request):
    account_form = RegisterForm(data=request.POST)
    if request.method == "POST" and account_form.is_valid():
        return render(request, 'register/confirm_data.html', {'account_form': account_form})
    else:
        return render(request, 'register/userinfo.html', {'account_form': account_form})
    
    #return render(request, 'register/confirm_data.html', {'account_form': account_form})

def final_signup(request):
    password_form = PasswordForm()
    return render(request, 'register/final_signup.html', {'password_form':password_form})

def submit_form(request):
    password_form = PasswordForm(data=request.POST)
    if request.method == "POST" and password_form.is_valid():
        if request.POST['password'] == request.POST['confirm_password']:
            return redirect('/register/confirmation_page')
        else:
            password_form = PasswordForm()
            message = "password do not match"
            return render(request, 'register/final_signup.html', {'password_form':password_form, 'message':message})
    else:
        return render(request, 'register/final_signup.html', {'password_form':password_form})
    #return render(request, 'register/submit_form.html', {})

def confirmation_page(request):
    return render(request, 'register/submit_form.html', {})
