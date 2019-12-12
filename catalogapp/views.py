from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product,Description

# Create your views here.


def index(request):
    products = Product.objects.all()
    for product in products:
        product.harga = '{:,}'.format(product.harga)

    return render(request,'catalogapp/index.html',{'products':products})

def product_detail(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    product.harga = '{:,}'.format(product.harga)
    descriptions = Description.objects.filter(product=product_id).all()
    ctx =  {
        'product': product,
        'descriptions': descriptions,
    }
    
    return render(request, 'catalogapp/detail.html', ctx)


def insert_product(request):
    return render(request, 'catalogapp/product_input.html',)

def save_new_product(request):
    if request.POST:
        nama = request.POST['product-name']
        harga = request.POST['product-harga']
        img_url = request.POST['product-img-url']

        proceed = Product(nama=nama, harga=harga, img_url=img_url)
        proceed.save()

        return redirect('/')
