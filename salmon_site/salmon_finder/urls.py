from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("find-serovar/", views.find_serovar, name="serovar_finder"),  # main app logic
]
