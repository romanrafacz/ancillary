from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(label='please enter email address', max_length=75)
    confirm_email = forms.EmailField(label='please confirm email address', max_length=75)
    
