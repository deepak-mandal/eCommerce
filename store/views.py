from django.shortcuts import render
#importing JSON response
from django.http import JsonResponse
import json


# Create your views here.
from .models import *


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer    #for one to one relationship
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems=order['get_cart_items']

    # Rendering all the added product from database to the main page
    product = Product.objects.all()
    context = {'products': product, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    #check if auth. user or guest user
    if request.user.is_authenticated:
        customer = request.user.customer    #for one to one relationship
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems=order['get_cart_items']


    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    # check if auth. user or guest user
    if request.user.is_authenticated:
        customer = request.user.customer  # for one to one relationship
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
        cartItems=order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)



def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']

    print("Action: ", action)
    print("productId", productId)

    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created=OrderItem.objects.get_or_create(order=order, product=product)

    if action=="add":
        orderItem.quantity=(orderItem.quantity + 1)
    elif action=="remove":
        orderItem.quantity=(orderItem.quantity -1)

    orderItem.save()

    if orderItem.quantity<=0:
        orderItem.delete()




    return JsonResponse("Item was added", safe=False)