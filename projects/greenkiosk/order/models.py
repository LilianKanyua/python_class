from django.db import models
from cart.models import Cart
from customer.models import Customer
from delivery.models import Delivery


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    shipment = models.ForeignKey(Delivery, null=True, on_delete=models.CASCADE)
    basket = models.ForeignKey(Cart, null= True, on_delete=models.CASCADE)
    products = models.CharField(max_length=255)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

# Create your models here.
