from django.contrib import admin
from .models import Product, Customer, CartProduct, Cart


admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(CartProduct)
admin.site.register(Cart)
