from django.contrib import admin

# Register your models here.
from ViageApp.models import *


admin.site.register(Config)
admin.site.register(TripPlanning)


class PlaceImagesAdmin(admin.ModelAdmin):
    list_filter = ('place',)
    list_display = ('place', 'images')
admin.site.register(PlaceImages,PlaceImagesAdmin)