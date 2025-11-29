from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.decorators import action
from core.helpers import serializer_saver , update_field , get_related_field
from .models import KampusUser
from .serializers import UserSerializer , MeSerializer
from .permissions import IsAdmin , IsCommAgent , IsStudent , IsStudentOrCommAgent
from django.core.exceptions import ObjectDoesNotExist
from commerce.serializers import ProductSerializer
from forum.serializers import EntrySerializer , EntryCommentSerializer , EntryLikeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = KampusUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # if self.action == 'create':
        #     return [AllowAny()]  
        # if self.action == 'update':
        #     return [IsAdmin()]
        # if self.action == 'me':
        #     return [IsStudentOrCommAgent()]
        # if self.action == 'change_role':
        #     return [IsAdmin()]
        # if self.action == 'list':
        #     return[IsAdmin()]
        # if self.action == 'retrieve':
        #     return[IsAuthenticated()]
        
        return [IsAuthenticated()]
    
    def list(self,request,*args,**kwargs):
        print(self.serializer_class.Meta.model.EMAIL_FIELD)
        return super().list(self,request, *args,**kwargs)
    
    def retrieve(self, request, pk=None):
        try : 
            user = KampusUser.objects.get(pk=pk)
        except ObjectDoesNotExist as exc:
            return Response({"detail" : {"UserDoesNotExist":'Can\'t find this page?'}}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        data = request.data.copy()
        serializer = serializer_saver(self.get_serializer_class(),
                                      user,
                                       data,
                                        partial=True )

        return Response(serializer.data)

    @action(detail=False, methods=['get','put'])
    def me(self, request):
        user = request.user
        if request.method == 'get':
            serializer = MeSerializer(user)
            return Response(serializer.data)
        
        
        serializer = serializer_saver(serializer_class=MeSerializer,
                                        instance=user , 
                                        data=request.data, 
                                        context={"request": request},
                                        partial=True)
            
        return Response(serializer.data)
    
    @action(detail=True , methods=['put'])
    def change_role(self,request, pk=None):
        data = {"Role" : request.data.get("Role")}
        ErrorName = "RoleNotFound"
        Error = "Can't find that role"
        response = update_field(self, request=request , pk=pk,data = data,
                                ErrorName=ErrorName, 
                                Error = Error
                                )    
        return response
    
    @action(methods=['get'] , detail=True)
    def products(self, request,pk):
        ErrorName = 'ProductsNotFound'
        Error = 'Could not find any product for this user?'
        
        response = get_related_field(self,serializer_class =ProductSerializer ,related_name='products' , ErrorName=ErrorName , Error=Error , pk=pk)    
        return response
    
    @action(methods=['get'] , detail=True)
    def entries(self,request,pk):
        ErrorName = 'EntriesNotFound'
        Error = 'Could not find any entry for this user?'

        response = get_related_field(self,serializer_class =EntrySerializer ,related_name='entries' , ErrorName=ErrorName , Error=Error , pk=pk)    
        return response
        
    
