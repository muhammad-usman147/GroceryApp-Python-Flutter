from django.db import models
from store.models import Owner_Products
from user.models import User
# Create your models here.
class Selling_history(models.Model):
    owner_product_id = models.ForeignKey('store.Owner_Products',
    on_delete=models.SET_NULL, null = True)
    owner_user_id = models.ForeignKey('user.User',
    on_delete=models.SET_NULL, 
    null = True)
    Quantity_sold = models.IntegerField()
    Date = models.DateField()
