from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets , status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from .models import Item
from .serializers import ItemSerializer
from core.helpers import serializer_saver
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.http import Http404
class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    @action(methods=['put' , 'patch'] , detail=True)
    def lost(self,request, pk):
        ErrorName = "ItemNotFound" 
        Error = "Can't Find This Page"
        data = {"item_found" : not item.item_found}
           