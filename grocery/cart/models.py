from django.db import models

# Create your models here.
class CartSystem(models.Model):
    quantity = models.IntegerField()
    address = models.CharField(max_length=100)
    date  = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    card_payment = models.CharField(max_length=100) 
    #either null , card type such as mastercard, visa, unionpay etc
    delivery_status = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    #Status = pending / in progress/ in-delivery / delivered
    owner_id = models.ForeignKey('store.Owner_table',on_delete=models.SET_NULL, null = True)
    user_id = models.ForeignKey('user.User',on_delete=models.SET_NULL, null = True)
    product_id = models.ForeignKey('store.Owner_Products',on_delete=models.SET_NULL, null = True)
