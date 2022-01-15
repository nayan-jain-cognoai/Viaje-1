# imports from packages
import logging
import os
import sys
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response

# imports from files
from Viage.utils_common import *
from ViageApp.models import Config,TripPlanning
from rest_framework.decorators import api_view, renderer_classes
import linecache
from inspect import getframeinfo, stack


logger = logging.getLogger(__name__)

try:
    import ujson as json
except ImportError as e:
    try:
        print(e)
        import simplejson as json
    except ImportError as e:
        print(e)
        import json
# Create your views here.

def index(request):
	try:
		raise_info("Inside Index Page")
		config_object = Config.objects.all()[0]
		return render(request, 'ViageApp/home/home.html',{
			"config_object":config_object
			})
	except Exception as e:
		raise_exception("HomePage has an error")
		return HttpResponse("We are facing some maintainance activity")
	

def HomePage(request):
	try:
		raise_info("Inside Home Page")
		return render(request,'ViageApp/trip_plan/home.html')
	except Exception as e:
		raise_exception("HomePage has an error")
		return HttpResponse("We are facing some maintainance activity")


def TripPlan(request):
	try:
		raise_info("Inside Trip Plan Page")
		return render(request,'ViageApp/trip_plan/tripplan.html')
	except Exception as e:
		raise_exception("Trip Plan has an error")
		return HttpResponse("We are facing some maintainance activity")

@api_view(('POST',))
def BookTrip(request):
	try:
		raise_info("Inside Book Trip Plan Page")
		data = request.data
		
		trip_plan_data = data['trip']
		pk = data['pk']

		if(pk == ""):
			trip_plan = TripPlanning.objects.create(trip_details=trip_plan_data)
			pk = trip_plan.pk
		else:
			trip_plan = TripPlanning.objects.get(pk=pk)
			trip_plan.trip_details = trip_plan_data
			trip_plan.save()
		pk = trip_plan.pk
		response = {"status_code":"200", "pk": pk}
		return Response(data=response)
	except Exception as e:
		raise_exception("Error in BookTrip")
		response = {"status_code":"500"}
		return Response(data=response)


def EditTrip(request):
	try:
		pk = request.GET["pk"]
		trip_plan_object = TripPlanning.objects.get(pk=pk).trip_details
		
		return render(request,'ViageApp/trip_plan/tripedit.html',{
			"trip_plan_object":trip_plan_object
			})
	except Exception as e:
		raise_exception("Error in EditTrip")
		return HttpResponse("We are facing some maintainance activity")



	