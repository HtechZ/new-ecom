from django.shortcuts import render
from .models import Product

# Create your views here.
def home_page(request):
    
    products = Product.objects.filter()
    context = {"products":products}
    return render(request, "home.html", context)