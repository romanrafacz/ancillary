from django.db import models

# Create your models here.

class Room_Details(models.Model):
    meeting_title = models.CharField('Meeting Title', max_length=50)
    request_date = models.DateField()
    location_name = models.CharField('Location Name', max_length=50)
    room_name = models.CharField('Room Name', max_length=50)
    location_address = models.CharField('Location Address', max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    attendance = models.IntegerField('Attendance', blank=True)
    est_budget = models.CharField('Est Budge', max_length=15, blank=True)
    seupt_style = models.CharField('Setup Style', max_length=50, blank=True)
