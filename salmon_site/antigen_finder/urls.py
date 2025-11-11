from django.urls import path
from . import views

urlpatterns = [
    path("find-antigen/", views.find_antigen_formula, name="antigen_finder"),  # main app logic
]
