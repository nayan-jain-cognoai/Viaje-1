# imports from packages
import logging
import os
import sys
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response

# imports from files
from Viage.utils_common import *
from ViageApp.models import Config,TripPlanning,PlaceImages
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

def raise_exception(message=''):
	exc_type, exc_obj, tb = sys.exc_info()
	caller = getframeinfo(stack()[1][0])
	logger.error("Error [%s] File: [%s]: at Line [%d] :-Message [%s]",exc_obj,caller.filename, caller.lineno, message)



def raise_info(message=''):
	caller = getframeinfo(stack()[1][0])
	logger.info("File: %s: at Line %d :- %s",caller.filename, caller.lineno, message)
	

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
		place_images = PlaceImages.objects.all()
		return render(request,'ViageApp/trip_plan/home.html',{
				"place_images":place_images
			})
	except Exception as e:
		raise_exception("HomePage has an error")
		return HttpResponse("We are facing some maintainance activity")


def TripPlan(request):
	try:
		raise_info("Inside Trip Plan Page")
		place_to_visit = request.GET["place_to_visit"]
		start_date = request.GET["start_date"]
		end_date = request.GET["end_date"]
		image_corresponding_to_place = PlaceImages.objects.filter(place=place_to_visit)[0].images

		return render(request,'ViageApp/trip_plan/tripplan.html',{
			"place_to_visit":place_to_visit,
			"image_corresponding_to_place":image_corresponding_to_place,
			"start_date":start_date,
			"end_date":end_date
			})
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
		place_to_visit = request.GET["place_to_visit"]
		start_date = request.GET["start_date"]
		end_date = request.GET["end_date"]
		image_corresponding_to_place = PlaceImages.objects.filter(place=place_to_visit)[0].images

		trip_plan_object = TripPlanning.objects.get(pk=pk).trip_details
		total_days = len(trip_plan_object)
		print(total_days)
		
		return render(request,'ViageApp/trip_plan/tripedit.html',{
			"trip_plan_object":trip_plan_object,
			"place_to_visit":place_to_visit,
			"image_corresponding_to_place":image_corresponding_to_place,
			"start_date":start_date,
			"end_date":end_date,
			"total_days":total_days
			})
	except Exception as e:
		raise_exception("Error in EditTrip")
		return HttpResponse("We are facing some maintainance activity")



	