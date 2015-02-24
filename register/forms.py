from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit


class RegisterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-example-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'check_email'



    email = forms.EmailField(label='please enter email address', max_length=75, error_messages={'required': 'Please enter a valid email'})
    confirm_email = forms.EmailField(label='please confirm email address', max_length=75)
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    job_title = forms.CharField(label='Job Title', max_length=50)
    comany = forms.CharField(label='Company', max_length=50)
    billing_address = forms.CharField(label='Billing Address', max_length=50)
    billing_address2 = forms.CharField(label='Billing Address 2', max_length=50, required=False)
    country = forms.CharField(label='Country', max_length=20)
    city = forms.CharField(label='City', max_length=20)
    state = forms.CharField(label='State', max_length=20)
    zip = forms.CharField(label='Zip', max_length=20)
    phone = forms.CharField(label='Phone', max_length=20)
    mobile= forms.CharField(label='Mobile Phone', max_length=20, required=False)
    cc_email = forms.EmailField(label='CC Email', required=False)
    password = forms.CharField(label='password', max_length=10)
    
