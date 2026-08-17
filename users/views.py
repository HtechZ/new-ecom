from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from .forms import Form
from django.contrib.auth import login,logout

# Create your views here.
def register_page(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            if email == "":user = User.objects.create_user(username=username,phone_number=phone_number)
            else:user = User.objects.create_user(username=username,phone_number=phone_number,email=email)
            login(request,user)
            return redirect("/")
    else:
        form = Form()
        context = {"form":form}
        return render(request, "register.html", context)
    
def login_page(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            phone_number = form.cleaned_data["phone_number"]
            user = User.objects.get(username=username,phone_number=phone_number)
            login(request,user)
            return redirect("/")
    else:
        form = Form()
        context = {"form":form}
        return render(request,"login.html",context)
    
def logout_page(request):
    logout(request)
    return redirect("/")