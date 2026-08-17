from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Order,OrderItem
from products.models import Product

# Create your views here.
def cart_page(request):
    if request.method == "POST":
        product_name = request.POST.get("product-name")
        if product_name:
            product = Product.objects.filter(name=product_name).first()
            order = Order.objects.filter(customer=request.user).first()
            if order == None:
                order = Order.objects.create(customer=request.user)
            order.full_price = order.full_price+int(product.price)
            order_item = OrderItem.objects.filter(order=order,item=product).first()
            if not order_item:
                order_item = OrderItem.objects.create(order=order,item=product)
            order_item.order_count = int(order_item.order_count)+1
            order.save()
            order_item.save()
        if request.POST.get("delete-item"):
            item_name = request.POST.get("delete-item")
            user_order = Order.objects.filter(customer=request.user).first()
            item = OrderItem.objects.filter(order=user_order,item__name=item_name).first()
            user_order.full_price = int(user_order.full_price)-(int(item.item.price)*int(item.order_count))
            user_order.save()
            item.delete()
            if len(OrderItem.objects.filter(order__customer=request.user))==0:
                user_order.delete()
            return redirect("/cart/")
        if request.POST.get("minus-one"):
            item_name = request.POST.get("minus-one")
            order = Order.objects.filter(customer=request.user).first()
            order_item = OrderItem.objects.filter(order__customer=request.user,item__name=item_name).first()
            order_item.order_count = int(order_item.order_count)-1
            order.full_price = int(order.full_price)-int(order_item.item.price)
            order.save()
            order_item.save()
            if order_item.order_count==0:
                order_item.delete()
            if len(OrderItem.objects.filter(order__customer=request.user))==0:
                order.delete()
            return redirect("/cart/")
        if request.POST.get("plus-one"):
            item_name = request.POST.get("plus-one")
            order_item = OrderItem.objects.filter(order__customer=request.user,item__name=item_name).first()
            order = Order.objects.filter(customer=request.user).first()
            order_item.order_count = int(order_item.order_count)+1
            order_item.save()
            order.full_price = int(order.full_price)+int(order_item.item.price)
            order.save()
            return redirect("/cart/")
        return redirect("/")
    else:
        order = Order.objects.filter(customer=request.user).first()
        if not order:
            return render(request, "cart.html")
        order_item = OrderItem.objects.filter(order=order)
        last_item = None
        if len(order_item)>1:
            last_item = order_item[len(order_item)-1]
        full_price_with_tax = order.full_price+(order.full_price)/10
        full_price_with_tax = int(full_price_with_tax) if full_price_with_tax%1==0 else full_price_with_tax==full_price_with_tax
        for order in order_item:
            if order.order_count==1:
                order.order_price = int(order.item.price)
            if order.order_count>1:
                order.order_price = int(order.item.price)*int(order.order_count)
        context = {"order":order,"order_item":order_item,"last_item":last_item,"full_price_with_tax":full_price_with_tax}
        return render(request, "cart.html", context)