from django.core.checks.messages import DEBUG
from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.db.models.enums import Choices
from django.db.models.fields import CharField, DateField, DateTimeField, TextField, URLField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django import forms
from multiselectfield import MultiSelectField
from django.utils import timezone

class Product(models.Model):
    name = CharField(max_length=100)
    description = TextField(max_length=300)
    image = ImageField(upload_to="products/images", null=True)
    url = URLField(blank=True)
    price = CharField(max_length=5, default='0')

    STORAGE_CHOICES =(
    ("64GB", "64GB"),
    ("128GB", "128GB"),
    ("256GB", "256GB"),
    ("512GB", "512GB"),
    (" "," ")
    )
    storage_options = MultiSelectField(choices = STORAGE_CHOICES, default=STORAGE_CHOICES[0])

    COLOR_CHOICES =(
    ("Red", "Red"),
    ("Blue", "Blue"),
    ("Matte-black", "Matte-black"),
    ("Silver", "Silver"),
    ("","")
    )
    color_options = MultiSelectField(choices = COLOR_CHOICES, default=COLOR_CHOICES[0])
    
    
    def __str__(self):
        return self.name

class Order(models.Model):
    item = models.ForeignKey(Product, on_delete=CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=CASCADE)
    color = models.CharField(max_length=20, default=None)
    storage = models.CharField(max_length=20, default=None)
    order_date = models.DateTimeField(default=None)

    def __str__(self):
        return str(self.item)
