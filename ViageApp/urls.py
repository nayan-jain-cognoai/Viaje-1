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
    path('signup/',views.SignUpUser,name="signup_user"),
    path('login/',views.LoginAPI,name="login_user"),
    path('logout/',views.Logout,name="log_out")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

