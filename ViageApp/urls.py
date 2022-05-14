from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.HomePage, name='homepage'),
    path('trip_plan/',views.TripPlan, name='trip_plan'),
    path('book_trip/',views.BookTrip, name='book_trip'),
    path('edit_trip/',views.EditTrip, name='edit_trip'),
    path('test_html/',views.TestHtml, name='test_html'),
    path('save-attachment/',views.SaveAttachments, name="save_attachments"),
    path('delete-attachment/',views.DeleteAttachments, name="delete_attachment"),
    path('signin/',views.SignUpUser,name="signup_user"),
    path('login/',views.LoginAPI,name="login_user"),
    path('logout/',views.Logout,name="log_out"),
    path('request_trip/',views.RaiseRequest,name="raise_request")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

