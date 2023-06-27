from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_home),
    path('echo/', views.api_echo),
]
