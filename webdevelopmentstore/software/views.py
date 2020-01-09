from django.shortcuts import render
from django.http import HttpResponse
from .models import softdes

# Create your views here.
def App(request):
	return HttpResponse("we are in development phase")