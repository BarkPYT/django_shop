from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, Http404, FileResponse
from random import randint
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .models import Product, Category, Order
import json
from django.db.models import Q
from .forms import OrderForm

def get_product(id: int):
    try:
        return Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404

def get_category(name: str):
    try:
        return Category.objects.get(name=name)
    except Category.DoesNotExist:
        raise Http404

@csrf_exempt
def products(request: HttpRequest):
    if request.method == 'GET':
        category_name = request.GET.get('category')

        products = Product.objects.all()

        if category_name is not None and category_name.strip() != '':
            category = Category.objects.filter(name__icontains=category_name).first()

            if category is None:
                products = products.filter(~Q(name__icontains = ''))
            else:
                products = products.filter(category = category)

        return render(request, 'products.html', {
            'title': 'Каталог',
            'products': products
        })
    
    if request.method == 'POST':
        body = json.loads(request.body.decode('UTF-8'))

        category = get_category(body['category'])

        product = Product(
            category = body['category'],
            name = body['name'],
            ser = body['ser']
            )
        
        return HttpResponse(str(product), status=200)

def product(request: HttpRequest, id: int):
    product = get_product(id)
    
    if request.method == 'GET':
        return render(request, 'product.html', {
            'title': product.name,
            'product': product
        })
    return HttpResponse(status=405)
    
def not_cat(request: HttpRequest):
    return FileResponse(
        open('D:/python/shop/static/media/cat.png', 'rb'),
    )

def index(request: HttpRequest):
    return render(request, 'index.html', {'title': 'Компьютерный магазин'})

@csrf_exempt
def make_order(request: HttpRequest, product_id:int):
    data = {
        'title': 'Оформление заказа',
        'form': OrderForm(),
        'product': get_product(product_id),
        'error': ''
    }
    if request.method == 'GET':
        return render(request, 'make_order.html', data)

    if request.method == 'POST':
        form = OrderForm( request.POST )

        if not form.is_valid():
            data['error'] = 'Данные заполнены неверно'
            return render(request, 'make_order.html', data)

        try:
            Order(**form.cleaned_data, product = get_product(product_id)).save()
        except Exception:
            data['error'] = 'Ошибка при сохранении заказа'
            data['form'] = form
        
        return redirect(reverse('product', kwargs={'id': product_id}))
    return redirect(reverse('products'))
        
    return HttpResponse(status=405)
