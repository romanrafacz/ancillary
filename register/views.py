from django.shortcuts import render, redirect
from django.http import HttpResponse

from register.forms import RegisterForm, EmailForm, PasswordForm, ReadOnlyForm

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
            #return redirect('/register/user_data')
            account_form = RegisterForm()
            return render(request, 'register/userinfo.html', {'new_account': new_account, 'account_form': account_form})
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

        # Initialize all values to be passed to confirm page
        lastname = account_form.cleaned_data['last_name']
        firstname = account_form.cleaned_data['first_name']
        job_title = account_form.cleaned_data['job_title']
        company = account_form.cleaned_data['company']
        billing_address = account_form.cleaned_data['billing_address']
        billing_address2 = account_form.cleaned_data['billing_address2']
        country = account_form.cleaned_data['country']
        city = account_form.cleaned_data['city']
        state = account_form.cleaned_data['state']
        zip = account_form.cleaned_data['zip']
        phone = account_form.cleaned_data['phone']
        mobile = account_form.cleaned_data['mobile']
        cc_email = account_form.cleaned_data['cc_email']

        ### created values to pass to confirmation page - may need a subclass that strips form of fields.  TBD
        form = { 'lastname': lastname, 'firstname': 'roman', 'job_title': job_title, 'company': company, 'billing_address': billing_address, 'billing_address2': billing_address } 
        form2 = { 'country': country, 'city': city, 'state':state, 'zip': zip, 'phone': phone, 'mobile': mobile, 'cc_email': cc_email }
        return render(request, 'register/confirm_data.html', {'account_form': account_form, 'form':form, 'form2':form2})
    else:
        account_form = RegisterForm()
        return render(request, 'register/userinfo.html', {'account_form': account_form})
    
    #return render(request, 'register/confirm_data.html', {'account_form': account_form})

def final_signup(request):
    password_form = PasswordForm()
    return render(request, 'register/final_signup.html', {'password_form':password_form})

def submit_form(request):
    password_form = PasswordForm(data=request.POST)
    if request.method == "POST" and password_form.is_valid():
        if request.POST['password'] == request.POST['confirm_password']:
            #myemail = request.POST['password']
            myemail = password_form['password']
            return render(request, 'register/submit_form.html', {'myemail':myemail})
        else:
            password_form = PasswordForm()
            message = "password do not match"
            return render(request, 'register/final_signup.html', {'password_form':password_form, 'message':message})
    else:
        return render(request, 'register/final_signup.html', {'password_form':password_form})

def confirmation_page(request):
    myemail = request.POST['password']
    return render(request, 'register/submit_form.html', {'myemail':myemail})
