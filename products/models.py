from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to="products/",blank=True,verbose_name="Product image")
    name = models.CharField(verbose_name="Product's name")
    about = models.TextField(verbose_name="Product's about")
    price = models.CharField(verbose_name="Product's price")
    weight = models.CharField(blank=True,verbose_name="Products's weight (in Gram)")
    height = models.CharField(blank=True,verbose_name="Products's height (in CentiMetre)")
    width = models.CharField(blank=True,verbose_name="Products's width (in CentiMetre)")
    special = models.BooleanField(default=False,verbose_name="Is this product special?")
    warranty = models.CharField(blank=True,verbose_name="Product's warranty")
    date = models.DateField(auto_now_add=True)
    buys = models.PositiveIntegerField(default=0,verbose_name="Product's buy counter")
    slug = models.SlugField(verbose_name="Product's link")