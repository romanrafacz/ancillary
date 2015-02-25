from django.shortcuts import render

from request.forms import RoomDetailsForm

# Create your views here.

def index(request):
    room_form = RoomDetailsForm()
    return render(request, 'request/index.html', {'room_form':room_form})
