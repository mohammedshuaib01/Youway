from django.contrib import admin

# Register your models here.
from store.models import Category, Size, Brand, Product, Order

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(Order)


