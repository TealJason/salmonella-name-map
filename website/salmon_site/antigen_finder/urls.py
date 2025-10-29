from django.urls import path
from . import views

urlpatterns = [
    path("find-antigen/", views.find_serovar, name="antigen_finder"),  # main app logic
]
