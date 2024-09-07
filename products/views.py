from django.http.response import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls.resolvers import get_resolver
from products.models import Product,Order
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.contrib import messages


def buypage(request):
    products = Product.objects.all()
    return render(request, 'buypage.html', {"products":products})

def buyitem(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'buyitem.html', {'product':product})

def createorder(request, product_id):
    
    main_order = get_object_or_404(Product, pk=product_id)
    col_list = []
    for x in main_order.color_options:
        col_list.append(x)

    stor_list = []
    for y in main_order.storage_options:
        stor_list.append(y)

    if request.user.is_authenticated:
        if request.method=='GET':
                return render(request, 'createorder.html', {'order':main_order, 'color_list':col_list, 'storage_list':stor_list})
        else:
            item = get_object_or_404(Product, pk=product_id)
            color = request.POST['color']
            storage = request.POST['storage']
            user = request.user
            date = timezone.now()
            neworder = Order(item=item, color=color, storage=storage, user=user,order_date=date)
            neworder.save()
            return render(request, 'confirmed.html', {'order':neworder, 'main_order':main_order})
        
    else:
        return render(request, 'buyitem.html', {'product':main_order,'error':'PLEASE LOGIN TO BUY'})
                    

def vieworders(request):
    all_orders = Order.objects.filter(user=request.user)
    return render(request, 'vieworders.html', {'allorders':all_orders}) 

def orderdetails(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orderdetails.html', {'order':order})
  
def cancelorder(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method=='POST':
        order.delete()
        return redirect('vieworders')
    