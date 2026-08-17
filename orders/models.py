from django.db import models
from users.models import User
from products.models import Product

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    full_price = models.PositiveIntegerField(default=0)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    order_count = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)