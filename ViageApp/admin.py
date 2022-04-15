from django.contrib import admin

# Register your models here.
from ViageApp.models import *

class PlaceImagesAdmin(admin.ModelAdmin):
    list_filter = ('place',)
    list_display = ('place', 'images', 'start_month', 'end_month','all_months')

admin.site.register(Config)
admin.site.register(TripPlanning)
admin.site.register(PlaceImages,PlaceImagesAdmin)
admin.site.register(User)
admin.site.register(RequestItineraries)