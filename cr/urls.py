from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/",home),  
    path("home/timetable/",tt),
    path("home/cancel/<int:id>",cancel),
    path("home/do-cancel/<int:id>",do_cancel),
    path("home/rooms/<int:id>",rooms),
    path("home/rooms/",prooms),
    path("home/history/",history),
    path('home/rooms/register/<int:room>/<int:id>/', registration_view,name='registration'),
    path("about/", about),
    path("feedback/",feedback,name='process_feedback'),
    path('success/', success, name='success_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)