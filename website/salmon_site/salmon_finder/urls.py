from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # landing page
    path("find-serovar/", views.find_serovar, name="serovar_finder"),  # main app logic
]
