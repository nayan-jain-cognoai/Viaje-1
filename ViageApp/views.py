# imports from packages
import logging
import os
import sys
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response

# imports from files
from Viage.utils_common import *
from ViageApp.models import Config,TripPlanning,PlaceImages,User
from rest_framework.decorators import api_view, renderer_classes
import linecache
from inspect import getframeinfo, stack
import os
from os import walk
from django.conf import settings
import shutil

from django.contrib.auth import authenticate, login, logout

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
		place_images = PlaceImages.objects.all()
		print(request.user)
		return render(request, 'ViageApp/home/home.html',{
			"config_object":config_object,
			"place_images":place_images
			})
	except Exception as e:
		raise_exception("HomePage has an error")
		return HttpResponse("We are facing some maintainance activity")
	

def HomePage(request):
	try:
		raise_info("Inside Home Page")
		place_images = PlaceImages.objects.all()
		place_to_visit = request.GET["place_to_visit"]
		start_date = request.GET["start_date"]
		end_date = request.GET["end_date"]
		image_corresponding_to_place = PlaceImages.objects.filter(place=place_to_visit)[0].images

		return render(request,'ViageApp/trip_plan/home.html',{
			"place_to_visit":place_to_visit,
			"image_corresponding_to_place":image_corresponding_to_place,
			"start_date":start_date,
			"end_date":end_date
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

def TestHtml(request):
	try:
		return render(request, 'ViageApp/test.html')
	except Exception as e:
		return HttpResponse("We are facing some maintainance activity")

@api_view(('POST',))
def SaveAttachments(request):
	try:
		data = request.data
		type_of_attachment = data["type_of_attachment"]
		id_of_attachment = data["id_of_attachment"]
		trip_pk = data["trip_pk"]
		file_id =  data["file_id"]
		filename = data["filename"]
		file_path = settings.DJANGO_DRF_FILEPOND_UPLOAD_TMP + "/" + id_of_attachment
		filenames = next(walk(file_path), (None, None, []))[2]  # [] if no file
		if filenames != []:
			full_file_path = file_path + "/" + filenames[0]


		os.rename(full_file_path,settings.MEDIA_ROOT + type_of_attachment + "/" + filename)

		#only for local
		sudoPassword = 'a1s2t3z4'
		command = "rm -rf "+settings.DJANGO_DRF_FILEPOND_UPLOAD_TMP + "/" + id_of_attachment
		remove_file = os.system('echo %s|sudo -S %s' % (sudoPassword, command))

		file_path = settings.MEDIA_ROOT + type_of_attachment + "/" + filename

		trip_object = TripPlanning.objects.get(pk=trip_pk)

		if type_of_attachment == "flights":
			
			flights = json.loads(trip_object.flights)
			flights.append(file_path)
			trip_object.flights = json.dumps(flights)

		elif type_of_attachment == "lodging":

			accomodation = json.loads(trip_object.accomodation)
			accomodation.append(file_path)
			trip_object.accomodation = json.dumps(accomodation)

		elif type_of_attachment == "cars":

			cars = json.loads(trip_object.cars)
			cars.append(file_path)
			trip_object.cars = json.dumps(cars)

		elif type_of_attachment == "bus":

			bus = json.loads(trip_object.bus)
			bus.append(file_path)
			trip_object.bus = json.dumps(bus)

		elif type_of_attachment == "train":

			train = json.loads(trip_object.train)
			train.append(file_path)
			trip_object.train = json.dumps(train)

		trip_object.save()
		response = {"status_code":"200", "pk": trip_pk}
		return Response(data=response)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		print(exc_tb.tb_lineno)
		raise_exception("Error in SaveAttachment")
		response = {"status_code":"500", "pk": trip_pk}
		return Response(data=response)

@api_view(('GET',))
def DeleteAttachments(request):
	try:
		data = request.GET
		trip_pk = data["trip_pk"]
		file_id = data["name_of_attachment"]
		type_of_attachment = data["type_of_attachment"]
			
		full_file_path = settings.MEDIA_ROOT + type_of_attachment + "/" + file_id

		# Only for local
		sudoPassword = 'a1s2t3z4'
		command = "rm -rf "+full_file_path
		remove_file = os.system('echo %s|sudo -S %s' % (sudoPassword, command))

		response = {"status_code":"200", "pk": trip_pk}

		return Response(data=response)
	except Exception as e:
		print(str(e))
		raise_exception("Error in DeleteAttachments")
		response = {"status_code":"500", "pk" : trip_pk}
		return Response(data=response)



@api_view(('POST',))
def SignUpUser(request):
	try:
		data = request.data
		response = {}
		full_name = data["full_name"]
		email_address = data["email_address"]
		password = data["password"]
		re_enter_password = data["re_enter_password"]
		if password != re_enter_password:
			response['status_code'] = "300"
			response['status_message'] = "Password dont match"
		if User.objects.filter(email=email_address):
			response['status_code'] = "400"
			response['status_message'] = "Email Address already exists"
			
		else:
			User.objects.create(first_name=full_name,email=email_address,password=password,username=email_address)
			response['status_code'] = 200
			response['status_message'] = "Success"
			


	except Exception as e:
		raise str(e)
		raise_exception("Error in SignUpUser")
		response = {"status_code":"500", "pk" : trip_pk}
	return Response(data=response)


@api_view(('POST',))
def LoginAPI(request):
	try:
		data = request.data
		response = {}
		email_address = data["email_address"]
		password = data["password"]
		# if user:
		print(email_address)
		print(password)
		user = authenticate(request,username=email_address,password=password)
		print(user)
		login(request, user,
                      backend='django.contrib.auth.backends.ModelBackend')
		response['status_code'] = "200"
		response['status_message'] = "Success"
		# else:
		# 	response['status_code'] = "400"
		# 	response["status_message"] = "User does not exist"




	except Exception as e:
		raise str(e)
		raise_exception("Error in SignUpUser")
		response = {"status_code":"500", "pk" : trip_pk}
	return Response(data=response)
	


	