from django.urls import path
from . import views

urlpatterns = [
    path('ai/analyze/', views.analyze_text, name='analyze_text'),
]
