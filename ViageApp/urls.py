from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.HomePage, name='homepage'),
    path('trip_plan/',views.TripPlan, name='trip_plan'),
    path('book_trip/',views.BookTrip, name='book_trip'),
    path('edit_trip/',views.EditTrip, name='edit_trip')
]
