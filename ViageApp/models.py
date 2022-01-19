from django.db import models
from django.contrib.postgres.fields import ArrayField

from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

from django_currentuser.db.models import CurrentUserField
from django.utils import timezone

# Create your models here.


class Config(models.Model):
	header_array = models.TextField(blank=True,default="EXCELLENT SERVICE,100 PERCENT TRUST,TOP ITINERARIES")
	header_content = models.TextField(blank=True,default="VIAGE IS A ONE STOP PLACE TO CREATE YOUR OWN ITINERARY, PUBLISH YOUR ITINERARY TO GET FEEDBACK FROM AGENTS, CONNECT WITH AGENT ON ONE TO ONE BASIS.")
	intro_header = models.TextField(blank=True,default="We Offer Some Of The Itinerary Service In Town")
	intro_content = models.TextField(blank=True,default="Select the itineraries and life jingalala, create your own, publish them or just select from the existing oness")
	ceo_config = models.TextField(blank=True,default="One stop platform for all travellers and agents")
	by_ceo = models.TextField(blank=True,default="Raj Sanghavi")
	strategy_array = models.TextField(blank=True,default="Environment Analysis $$$ Development Planning $$$ Execution & Evaluation")
	strategy_content_array = models.TextField(blank=True,default="The starting point of any success story is knowing your current position in the business environment $$$ After completing the environmental analysis the next stage is to design and  plan your development strategy $$$ In this phase you will focus on executing the actions plan and evaluating the results after each marketing campaign")
	acceleration_content = models.TextField(blank=True,default="Accelerate Business Growth To Improve Revenue Numbers")
	acceleration_content_header_array = models.TextField(blank=True,default="How Can Aria Help Your Business $$$ Great Strategic Business Planning $$$ Online Marketing Campaigns")
	acceleration_content_array = models.TextField(blank=True,default="The starting point of any success story is knowing your current position in the business environment $$$ After completing the environmental analysis the next stage is to design and  plan your development strategy $$$ In this phase you will focus on executing the actions plan and evaluating the results after each marketing campaign")
	contact_header = models.TextField(blank=True,default="Have Us Contact You By Filling And Submitting The Form")
	contact_content = models.TextField(blank=True,default="You are just a few steps away from a personalized offer. Just fill in the form and send it to us and we'll get right back with a call to help you decide what service package works.")
	contact_bullets = models.TextField(blank=True,default="It's very easy just fill in the form so we can call $$$ During the call we'll require some info about the company $$$ Don't hesitate to email us for any questions or inquiries")
	interested_in_options = models.TextField(blank=True,default="It's very easy just fill in the form so we can call $$$ During the call we'll require some info about the company $$$ Don't hesitate to email us for any questions or inquiries")
	agree_policy = models.TextField(blank=True,default="I agree to Viage's policy to use personal information to call me for details")
	footer = models.TextField(blank=True,default="© 2021 All Right Reserved")

	def save(self, *args, **kwargs):
		super(Config, self).save(*args, **kwargs)

	class Meta:
        verbose_name = 'Config'
        verbose_name_plural = 'Config'


class TripItinerary(models.Model):
	date = models.DateField(default=timezone.now,blank=False)
	trip_details = models.JSONField()

	def save(self, *args, **kwargs):
		super(TripItinerary, self).save(*args, **kwargs)

	class Meta:
        verbose_name = 'TripItinerary'
        verbose_name_plural = 'TripItinerary'

class TripPlanning(models.Model):
	date = models.DateField(default=timezone.now,blank=False)
	trip_details = models.JSONField(default={})

	def save(self, *args, **kwargs):
		super(TripPlanning, self).save(*args, **kwargs)

	class Meta:
        verbose_name = 'TripPlanning'
        verbose_name_plural = 'TripPlanning'

class PlaceImages(models.Model):
	place = models.TextField(default="")
	images = models.TextField(default="")

	def save(self,*args,**kwargs):
		super(PlaceImages,self).save(*args, **kwargs)

	class Meta:
        verbose_name = 'PlaceImages'
        verbose_name_plural = 'PlaceImages'


	

