from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit


class RegisterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-example-form'
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.form_action = '/register/confirm_data/'
        self.helper.add_input(Submit('submit', 'Submit'))

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

class EmailForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-example-form'
        self.helper.form_class = 'form-inline'
        self.helper.form_methog = 'post'
        self.helper.form_action = '/register/check_email/'
        self.helper.form_show_errors=True
        self.helper.form_error_title= 'emails do not match'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    email = forms.EmailField(label='please enter email address', max_length=75, error_messages={'required': 'Please enter a valid email'})
    confirm_email = forms.EmailField(label='please confirm email address', max_length=75)

class PasswordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-example-form'
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.form_action = '/register/submit_form/'
        self.helper.add_input(Submit('submit', 'Submit'))

    password = forms.CharField(label='Password', max_length=15)
    confirm_password = forms.CharField(label='Confirm Password', max_length=15)
