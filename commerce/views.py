from rest_framework import viewsets , status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from .models import Product , ProductCategory
from .serializers import ProductSerializer , ProductCategorySerializer
from rest_framework.decorators import action
from core.helpers import serializer_saver , update_field , get_related_field
from django.shortcuts import get_object_or_404
from django.http import Http404
# Create your views here.
class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    
    @action(methods=['get'] , detail=True)
    def get_products(self,request,pk=None):
        ErrorName = "ProductsDoesNotFound"
        Error = "There is no any product of this category."
        response = get_related_field(self,serializer_class=ProductSerializer,related_name='products',ErrorName=ErrorName , Error=Error , pk=pk)
        return response
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    @action(methods=['put'] , detail=True)
    def sold(self, request ,pk=None):
        ErrorName = "ProductNotFound" 
        Error = "Can't find that product"
        data = {"product_sold" : True}
        response = update_field(self,request=request,pk=pk,data=data,ErrorName=ErrorName,Error=Error)
        return response