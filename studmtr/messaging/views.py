from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Message
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import CreateMessageForm

@login_required
def chat(request,pk):
	form = CreateMessageForm()
	if request.method == 'POST':
	   form = CreateMessageForm(request.POST)
	   form.instance.sender = request.user
	   form.instance.reciever = return_user(pk)
	   if form.is_valid():
		   form.save()
		   return redirect('chat',pk)
	else:
		form = CreateMessageForm()	
	context = {
	'chats': (Message.objects.filter(sender = pk).filter(reciever = request.user)|Message.objects.filter(sender = request.user).filter(reciever = pk)).order_by('created_at'),
	'form':form
	}
	return render(request,'messaging/chat.html',context)

@login_required
def chats(request):
	a = []
	for i in User.objects.exclude(id = request.user.id):
		a.append(i.id)
	
	emp = []
	for i in a:
		emp.append(Message.objects.filter(reciever = request.user).filter(sender = i).last())

	context = {
		'chats':emp,
	}
	
	return render(request,'messaging/chats.html',context)



def return_user(pk):
	for i in User.objects.all():
		if i.id == pk:
			return i