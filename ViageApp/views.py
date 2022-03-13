# imports from packages
import logging
import os
import sys
import random

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
		strategy_array = config_object.strategy_array.split("$$$")
		strategy_content_array = config_object.strategy_content_array.split("$$$")
		strategy_array_images = config_object.strategy_array_images.split("$$$")


		final_strategy_content = zip(strategy_array,strategy_content_array,strategy_array_images)
		print(final_strategy_content)
		return render(request, 'ViageApp/home/home.html',{
			"config_object":config_object,
			"place_images":place_images,
			"final_strategy_content":final_strategy_content
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
		image_corresponding_to_place = image_corresponding_to_place.split(",")
		image_corresponding_to_place = random.choice(image_corresponding_to_place)		

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
		if request.user.is_authenticated:
			raise_info("Inside Trip Plan Page")
			place_to_visit = request.GET["place_to_visit"]
			start_date = request.GET["start_date"]
			end_date = request.GET["end_date"]
			image_corresponding_to_place = PlaceImages.objects.filter(place=place_to_visit)[0].images
			image_corresponding_to_place = image_corresponding_to_place.split(",")
			image_corresponding_to_place = random.choice(image_corresponding_to_place)
			dont_allow_attachment_to_save = True
			important_things_for_trip = {}
			default_start_budget = 5000
			default_end_budget = 5000

			return render(request,'ViageApp/trip_plan/tripplan.html',{
				"place_to_visit":place_to_visit,
				"image_corresponding_to_place":image_corresponding_to_place,
				"start_date":start_date,
				"end_date":end_date,
				"dont_allow_attachment_to_save":dont_allow_attachment_to_save,
				"important_things_for_trip":important_things_for_trip,
				"start_budget":default_start_budget,
				"end_budget":default_end_budget
				})
		else:
			return HttpResponse("You are not authenticated to use this page.")
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
		user_pk = data['user_pk']
		important_things_for_trip = data['important_things_for_trip']
		user = User.objects.get(pk=user_pk)
		start_budget = data['start_budget']
		end_budget = data['end_budget']

		if(pk == ""):
			trip_plan = TripPlanning.objects.create(trip_details=trip_plan_data,
													user=user,
													important_things_for_trip=important_things_for_trip,
													start_budget=start_budget,
													end_budget=end_budget)
			pk = trip_plan.pk
		else:
			trip_plan = TripPlanning.objects.get(pk=pk)
			trip_plan.trip_details = trip_plan_data
			trip_plan.important_things_for_trip = important_things_for_trip
			trip_plan.start_budget = start_budget
			trip_plan.end_budget = end_budget
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
		image_corresponding_to_place = image_corresponding_to_place.split(",")
		image_corresponding_to_place = random.choice(image_corresponding_to_place)

		trip_plan_object = TripPlanning.objects.get(pk=pk)
		trip_details = trip_plan_object.trip_details
		total_days = len(trip_details)
		important_things_for_trip = trip_plan_object.important_things_for_trip
		start_budget = trip_plan_object.start_budget
		end_budget = trip_plan_object.end_budget
		files_flight = json.loads(trip_plan_object.flights)
		files_accomadation = json.loads(trip_plan_object.accomodation)
		files_cars = json.loads(trip_plan_object.cars)
		files_train = json.loads(trip_plan_object.train)
		files_bus = json.loads(trip_plan_object.bus)

		final_file_list = files_flight + files_accomadation + files_cars + files_train + files_bus

		return render(request,'ViageApp/trip_plan/tripedit.html',{
			"trip_plan_object":trip_details,
			"place_to_visit":place_to_visit,
			"image_corresponding_to_place":image_corresponding_to_place,
			"start_date":start_date,
			"end_date":end_date,
			"total_days":total_days,
			"important_things_for_trip":important_things_for_trip,
			"start_budget":start_budget,
			"end_budget":end_budget,
			"final_file_list" : final_file_list,
			
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

		http_host_with_files = "/files/"
		file_path_to_append =  http_host_with_files + type_of_attachment + "/" + filename

		if type_of_attachment == "flights":
			flights = json.loads(trip_object.flights)
			flights.append(file_path_to_append)
			trip_object.flights = json.dumps(list(set(flights)))

		elif type_of_attachment == "lodging":

			accomodation = json.loads(trip_object.accomodation)
			accomodation.append(file_path_to_append)
			trip_object.accomodation = json.dumps(list(set(accomodation)))

		elif type_of_attachment == "cars":

			cars = json.loads(trip_object.cars)
			cars.append(file_path_to_append)
			trip_object.cars = json.dumps(list(set(cars)))

		elif type_of_attachment == "bus":

			bus = json.loads(trip_object.bus)
			bus.append(file_path_to_append)
			trip_object.bus = json.dumps(list(set(bus)))

		elif type_of_attachment == "train":

			train = json.loads(trip_object.train)
			train.append(file_path_to_append)
			trip_object.train = json.dumps(list(set(train)))

		trip_object.save()
		response = {"status_code":"200", "pk": trip_pk}
		return Response(data=response)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
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

		trip_object = TripPlanning.objects.get(pk=trip_pk)

		http_host_with_files = "/files/"
		file_path_to_append =  http_host_with_files + type_of_attachment + "/" + file_id

		if type_of_attachment == "flights":
			flights = json.loads(trip_object.flights)
			flights.remove(file_path_to_append)
			trip_object.flights = json.dumps(list(set(flights)))

		elif type_of_attachment == "lodging":

			accomodation = json.loads(trip_object.accomodation)
			accomodation.remove(file_path_to_append)
			trip_object.accomodation = json.dumps(list(set(accomodation)))

		elif type_of_attachment == "cars":

			cars = json.loads(trip_object.cars)
			cars.remove(file_path_to_append)
			trip_object.cars = json.dumps(list(set(cars)))

		elif type_of_attachment == "bus":

			bus = json.loads(trip_object.bus)
			bus.remove(file_path_to_append)
			trip_object.bus = json.dumps(list(set(bus)))

		elif type_of_attachment == "train":

			train = json.loads(trip_object.train)
			train.remove(file_path_to_append)
			trip_object.train = json.dumps(list(set(train)))

		trip_object.save()

		response = {"status_code":"200", "pk": trip_pk}

		return Response(data=response)
	except Exception as e:
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
		user = authenticate(request,username=email_address,password=password)
		login(request, user,
                      backend='django.contrib.auth.backends.ModelBackend')
		response['status_code'] = "200"
		response['status_message'] = "Success"
		
	except Exception as e:
		raise str(e)
		raise_exception("Error in SignUpUser")
		response = {"status_code":"500", "pk" : trip_pk}
	return Response(data=response)
	


	