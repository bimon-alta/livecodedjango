from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product,Description

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request,'catalogapp/index.html',{'products':products})

def product_detail(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    descriptions = Description.objects(product=product)
    ctx =  {
        'product': product,
        'descriptions': descriptions,
    }
       

    
    return render(request, 'catalogapp/detail.html', ctx)

