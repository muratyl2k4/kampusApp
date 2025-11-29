from django.contrib import admin
from .models import Product , ProductCategory , ProductStatus

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductStatus)

# Register your models here.
