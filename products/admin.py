from django.contrib import admin
from products.models import ProductCategory, Product
from django import db

db.connections.close_all()
admin.site.register(Product)
admin.site.register(ProductCategory )