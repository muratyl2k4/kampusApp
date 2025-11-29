from rest_framework import viewsets , status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.decorators import action 
from .models import Community , CommunityAnnouncement
from .serializers import CommunitySerializer , CommunityAnnouncementSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404
from core.helpers import get_related_field

# Create your views here.


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    
    @action(methods=['get'] , detail=True)
    def get_announcements(self,request,pk=None):
        ErrorName = "CommunityAnnouncementNotFound"
        Error = "There is no any announcement for this community"
        response = get_related_field(self,CommunityAnnouncementSerializer,related_name='announcements',ErrorName=ErrorName , Error=Error , pk=pk)
        
        return response

class CommunityAnnouncementViewSet(viewsets.ModelViewSet):
    queryset = CommunityAnnouncement.objects.all()
    serializer_class = CommunityAnnouncementSerializer