from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from django.utils import timezone
from django import contrib
from .models import Profile

def register(request):
	if request.method == 'POST':
	   form = UserRegisterForm(request.POST)
	   if form.is_valid():
		   form.save()
		   username = form.cleaned_data.get('username')
		   messages.success(request,f'Your Account has been created !You are now able to login ')
		   return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request,'users/register.html',{'form':form})
	
@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,instance  = request.user)
		p_form = ProfileUpdateForm(request.POST,
								   request.FILES,
								   instance = request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your Account has been Updated !')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.profile)

	context = {
		'u_form':u_form,
		'p_form':p_form
	}
	return render(request,'users/profile.html',context)

def user_profile(request,pk):
	context = {
	'var': Profile.objects.filter(id = pk).first()
	}
	return render(request,'users/user_profile.html',context)

def profiles(request):
	context = {
	'vars':Profile.objects.exclude(id = request.user.id)
	}
	return render(request,'users/profiles.html',context)