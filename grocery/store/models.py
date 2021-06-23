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
    
class Owner_Products(models.Model):
    #Owner_Product
    owner_id = models.ForeignKey('Owner_table',on_delete=models.SET_NULL,null=True)
    item_name = models.CharField(max_length=100)
    item_picture_path = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price_to_sold = models.IntegerField()
    Quantity_type = models.CharField(max_length=100)
