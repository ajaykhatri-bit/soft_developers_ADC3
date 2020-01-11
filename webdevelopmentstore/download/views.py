from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import App
from .models import Device
# Create your views here.
def homepage(request):
	aps = app.object.all()
	dev = device.object.all()
	return render(request, 'main/home.html', context={'aps':'aps'})
	return render(request, 'main/home.html', context={'dev':'dev'})
	