from django.urls import path
from products import views
import products

app_name = 'products'

urlpatterns = [
    path('',views.buypage, name='products'),
    path('buyitem/', products.views.buypage, name='buypage'),
    path('buyitem/<int:product_id>/',products.views.buyitem, name='buyitem'),



    
]