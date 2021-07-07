from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class Biker_Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    number = models.BigIntegerField()
    password = models.CharField(max_length=100)

class OrderBiker(models.Model):
    order_id_to_biker = models.ForeignKey('cart.CartSystem',
    on_delete=models.SET_NULL,
    null = True)
    biker_id = models.ForeignKey('Biker_Profile',
    on_delete=models.SET_NULL,
    null= True)
    delivery_status = models.CharField(max_length=100)
    