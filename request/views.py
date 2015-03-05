from django.shortcuts import render
from django.http import HttpResponse

from request.forms import RoomDetailsForm
from request.models import Room_Details

# Create your views here.

def index(request):
    room_form = RoomDetailsForm()
    return render(request, 'request/index.html', {'room_form':room_form})

def submit_request(request):
    room_form = RoomDetailsForm(data=request.POST)
    requested_data = Room_Details.objects.all()
    if request.method == "POST" and room_form.is_valid():
        room_data = Room_Details(meeting_title=request.POST['meeting_title'], request_date=request.POST['request_date'], location_name=request.POST['location_name'], room_name=request.POST['room_name'], location_address=request.POST['location_address'], start_date=request.POST['start_date'], end_date=request.POST['end_date'], start_time=request.POST['start_time'], end_time=request.POST['end_time'], attendance=request.POST['attendance'], est_budget=request.POST['est_budget'], setup_style=request.POST['setup_style']) 
        room_data.save()
        return render(request, 'request/submit_success.html', {'requested_data':requested_data})
    else:
        return HttpResponse('something off')

    #return render(request, 'request/index.html', {'room_form':room_form})

def new_request(request):
    return render(request, 'request/new_request_page.html', {})
