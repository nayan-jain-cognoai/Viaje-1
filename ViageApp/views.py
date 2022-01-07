# imports from packages
import logging
import os
import sys
from django.shortcuts import render
from django.http import HttpResponse

# imports from files
from Viage.utils_common import *
from ViageApp.models import Config


# Create your views here.

def index(request):
	try:
		config_object = Config.objects.all()[0]
		return render(request, 'ViageApp/home/home.html',{
			"config_object":config_object
			})
	except Exception as e:
		raise_exception("HomePage has an error")
	

def HomePage(request):
	try:
		return render(request,'ViageApp/trip_plan/home.html')
	except Exception as e:
		raise_exception("HomePage has an error")
		return HttpResponse("We are facing some maintainance activity")

def TripPlan(request):
	try:
		return render(request,'ViageApp/trip_plan/tripplan.html')
	except Exception as e:
		raise_exception("Trip Plan has an error")
		return HttpResponse("We are facing some maintainance activity")

	