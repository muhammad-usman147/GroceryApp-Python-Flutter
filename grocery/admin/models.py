from django.db import models
from django.db.models.base import Model
# Create your models here.
class OwnerTable(models.Model):
    name = models.TextField()
    username = models.CharField()
    store_name = models.CharField(max_length=100)
    type = models.TextField()
    contact = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=100)


class OwnerProduct(models.Model):
    owner_id =  models.ForeignKey('OwnerTable',
    on_delete= models.SET_NULL,
    null = True
    )
    item_name = models.TextField(max_length=100),
    item_picture = models.TextField(),
    Quantity = models.CharField(max_length=10),
    solding_price = models.CharField(max_length=10),
    type = models.CharField(max_length = 100)