from django.db import models

# Create your models here.
class Place_Name(models.Model):
    user_place_lookup_name = models.CharField(max_length=50)

