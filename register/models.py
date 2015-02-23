from django.db import models

# Create your models here.

class Register(models.Model):
    email = models.EmailField('email')
    first_name = models.CharField('First Name', max_length=25)
    last_name = models.CharField('Last Name', max_length=25)
    job_title = models.CharField('Job Title', max_length=20)
    comany = models.CharField('Company', max_length=20)
    billing_address = models.CharField('Billing Address', max_length=50)
    billing_address2 = models.CharField('Billing Address 2', max_length=50, blank=True)
    country = models.CharField('Country', max_length=20)
    city = models.CharField('City', max_length=20)
    state = models.CharField('State', max_length=20)
    zip = models.CharField('Zip', max_length=20)
    phone = models.CharField('Phone', max_length=20)
    mobile= models.CharField('Mobile Phone', max_length=20, blank=True)
    cc_email = models.EmailField('CC Email', blank=True)
    password = models.CharField('password', max_length=10)
