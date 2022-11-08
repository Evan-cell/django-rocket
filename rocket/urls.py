from django.urls import path

from . import views

urlpatterns = [
    path('', views.rocket, name="rocket")
]