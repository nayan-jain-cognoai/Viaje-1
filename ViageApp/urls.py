from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.HomePage, name='homepage'),
    path('trip_plan/',views.TripPlan, name='trip_plan')
]
