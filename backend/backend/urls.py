from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Citizen Report Tracker Backend!")

urlpatterns = [
    path('', home),  # <-- root URL
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
