from ViageApp.models import *
pl = PlaceImages.objects.filter(pk=122)[0]
pl.start_month = 3
pl.save()
