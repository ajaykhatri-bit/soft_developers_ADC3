from django.shortcuts import render, redirect
from django.http import HttpResponse
#from .models import App
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import OurForm
from django.contrib import messages
# Create your views here.



def register(request):
	if request.method == "post":
		form = OurForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('main: homepage')



	form = OurForm()
	return render(request, "main/register.html", context={"form": form})



def user_logout(request):
	logout(request)
	return redirect('main:homepage')


def user_login(request):
	if request.method == "post":
		form = AuthenticationForm(request, data=request.Post)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(user=username, password=password)

			if user is not None:
				login(request, user)
				messages.success(request, f'you have logged as {{username}}')
				return redirect('main:homepage')


	form = AuthenticationForm()
	return render(request,"main/login.html", context={"form": form})