from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from .models import Product
def index(request:HttpRequest):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})

def new(request:HttpRequest):
    return HttpResponse('new product ')