from django.db import models
from accounts.models import KampusUser
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=120 , unique=True)

    def __str__(self):
        return self.category_name

class ProductStatus(models.Model):
    status = models.CharField(max_length=120 , unique=True)
     
def product_image_path(instance, filename):
    
    return f"products/images/{instance.id}-{filename}"
class Product(models.Model):
    product_user = models.ForeignKey(KampusUser , on_delete=models.CASCADE , blank=False , related_name='products')
    product_category = models.ForeignKey(ProductCategory , on_delete=models.CASCADE , blank=False , related_name='products')
    product_image = models.ImageField(upload_to=product_image_path)
    product_title = models.CharField(max_length=120, blank=False)
    product_price = models.IntegerField(blank=False)
    product_text = models.TextField(blank=False)
    product_status = models.ForeignKey(ProductStatus ,default=1 ,on_delete=models.SET_DEFAULT ,null=True, blank=False , related_name='products')
    product_date = models.DateTimeField(auto_now=True , blank=False)
    product_sold = models.BooleanField(default=False)
    def __str__(self):
        return self.product_title
# Create your models here.
