from rest_framework import viewsets , status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from .models import Entry , EntryComment , Topic , EntryLike
from .serializers import EntrySerializer , EntryCommentSerializer  ,EntryLikeSerializer, TopicSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.decorators import action
from core.helpers import get_related_field
# Create your views here.

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    @action(methods=['get'] , detail=True)
    def get_entries(self, request ,pk=None):
        ErrorName = "EntriesNotFound"
        Error = "Could not find any entries for this topic"
        response = get_related_field(self,serializer_class=EntrySerializer,related_name='entries',ErrorName=ErrorName , Error=Error , pk=pk)

        return response
        


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    @action(methods=['get'] , detail=True)
    def get_comments(self,request,pk=None):
        ErrorName = "CommentsNotFound"
        Error = "There is no any comment for this entry"
        response = get_related_field(self,serializer_class=EntryCommentSerializer ,related_name='comments',ErrorName=ErrorName , Error=Error , pk=pk)
        
        return response
    
    @action(methods=['get'] , detail=True)
    def get_likes(self,request,pk=None):
        ErrorName = "LikesNotFound"
        Error = "There is no any likes for this entry"
        response = get_related_field(self,serializer_class=EntryLikeSerializer ,related_name='comments',ErrorName=ErrorName , Error=Error , pk=pk)
        
        return response
        
        
        
        
    
class EntryLikeViewSet(viewsets.ModelViewSet):
    queryset = EntryLike.objects.all()
    serializer_class = EntryLikeSerializer
    @action(methods=['delete'] , detail=True)
    def remove_like(self,request,pk=None):
        try : 
            data = get_object_or_404(self.serializer_class.Meta.model , pk=pk)
            data.delete()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=204)

class EntryCommentViewSet(viewsets.ModelViewSet):
    queryset= EntryComment.objects.all()
    serializer_class = EntryCommentSerializer

