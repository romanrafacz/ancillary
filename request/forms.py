from django.forms import ModelForm
from request.models import Room_Details

class RoomDetailsForm(ModelForm):
    class Meta:
        model = Room_Details
        fields = ['meeting_title', 'request_date', 'location_name', 'room_name', 'location_address', 'start_date', 'end_date', 'start_time', 'end_time', 'attendance', 'est_budget', 'setup_style']

