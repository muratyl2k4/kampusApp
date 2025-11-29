from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from .models import DiscountAnnouncement
from .serializers import DiscountAnnouncementSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    serializer_class = DiscountAnnouncementSerializer
    queryset = DiscountAnnouncement.objects.all()