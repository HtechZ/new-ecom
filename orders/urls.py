from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('', views.cart_page, name="cart_page")
]