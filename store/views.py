from django.shortcuts import render

# Create your views here.
from .models import *


def store(request):
    # Rendering all the added product from database to the main page
    product = Product.objects.all()
    context = {'products': product}
    return render(request, 'store/store.html', context)


def cart(request):
    #check if auth. user or guest user
    if request.user.is_authenticated:
        customer = request.user.customer    #for one to one relationship
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    # check if auth. user or guest user
    if request.user.is_authenticated:
        customer = request.user.customer  # for one to one relationship
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)
