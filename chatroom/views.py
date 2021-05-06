from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib import messages

def home(request):
	return render(request,'chatroom/home.html')

def create_room(request):
	form = Create_roomname_form()
	if request.method == 'POST':
		New_room = request.POST.get('New_room')

		if Room_name.objects.filter(Name=New_room):
			messages.error(request,'This Room name already exists')

		elif ' ' in New_room or '!' in New_room:
			messages.error(request,'Sorry, try re-entering without any spaces or exclamation marks ')

		else:
			Room_name.objects.create(Name=New_room)
			messages.info(request,'Your room has successfully been created. You can join the created room from the form below')
			return redirect('join_room')

	return render(request , 'chatroom/create_room.html')

def join_room(request):
	try:
		context={}
		if request.method=='POST':
			room_name=request.POST.get('roomname')
			username = request.POST.get('username')

			Room_name.objects.get(Name =room_name)
			return HttpResponseRedirect(reverse('chatpage',args=[room_name,username]))
	except:
		messages.info(request,'Sorry Room Name does not exist')
	return render(request,'chatroom/join_room.html',context)


def chatpage(request,room_name,username):
	context = {'room_name':room_name,'username':username}
	return render(request,'chatroom/chatpage.html',context)
# Create your views here.
