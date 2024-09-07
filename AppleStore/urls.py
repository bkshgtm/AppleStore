"""mainstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import products
from products.views import createorder
import storefront
from django.contrib import admin
from django.urls import path,include
from storefront import views
from products.views import buyitem
from . import settings
from django.conf.urls.static import static
urlpatterns = [

    #AUTH
    path('admin/', admin.site.urls),
    path('signup/', storefront.views.signupuser, name ='signupuser'),
    path('logout/', storefront.views.logoutuser, name ='logoutuser'),
    path('login/', storefront.views.loginuser, name ='loginuser'),

    #PRODUCTS
    path('products/', include('products.urls')),
    
    #ORDER
    path('createorder/<int:product_id>/', products.views.createorder, name='createorder'),
    path('confirmed/<int:product_id>/', products.views.createorder, name='confirmed'),
    path('allorders', products.views.vieworders, name='vieworders'),
    path('allorders/order/<int:order_id>/', products.views.orderdetails, name='orderdetails'),
    path('allorders/order/cancelorder/<int:order_id>/', products.views.cancelorder, name='cancelorder'),

    #MISC
    path('', storefront.views.home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)