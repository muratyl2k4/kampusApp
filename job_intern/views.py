from rest_framework import viewsets , status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated , AllowAny
from .models import InternPlace , InternAnnouncement
from django.shortcuts import get_object_or_404

from django.http import Http404
from .serializers import InternPlaceSerializer , InternAnnouncementSerializer

from core.helpers import serializer_saver , update_field

class InternPlaceViewSet(viewsets.ModelViewSet):
    queryset = InternPlace.objects.all()
    serializer_class = InternPlaceSerializer
    @action(methods=['get'] , detail=True)
    def get_internships(self , request , pk=None):
        try : 
            data = get_object_or_404(self.serializer_class.Meta.model , pk=pk)
            data=  data.intern_announcements.all()
            
            serializer = InternAnnouncementSerializer(data, many=True)
        except Http404:
            
            return Response({"detail" : {"InternPlaceDoesNotExist" : "Can't find this page?"}} ,status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)


    


class InternAnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = InternAnnouncementSerializer
    queryset=  InternAnnouncement.objects.all()

    @action(methods=['put','patch'] , detail=True)
    def end(self,request,pk=None):
        data = {"intern_end" : True}
        ErrorName = "AnnouncementNotFound" 
        Error = "Can't find that page?"
        response = update_field(self,request=request,pk=pk,data=data,ErrorName=ErrorName,Error=Error)
        return response
        
    






