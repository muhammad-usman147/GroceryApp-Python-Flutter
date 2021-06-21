from django.db import models

# Create your models here.

class Owner_table(models.Model):
    #GROCERY OWNER 
    owner_name = models.CharField(max_length=100)
    owner_username = models.CharField(max_length=100)
    owner_email = models.EmailField()
    owner_password = models.CharField(max_length=100)
    owner_store_name = models.CharField(max_length=100)
    owner_store_type = models.CharField(max_length=100)
    owner_store_password = models.CharField(max_length=100)
    