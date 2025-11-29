#gece 3te kendi kendime neden ayni seyleri her methodun icinde ayri ayri yaziyorum diye
#sorarken olusturdugum dosya...
from rest_framework.response import Response
from rest_framework import serializers
from PIL import Image
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status



def serializer_saver(serializer_class, instance, data, *, context=None, partial=False):
    serializer = serializer_class(instance, data=data, partial=partial, context=context)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return serializer

def validate_image(image , * , min_h , min_w , max_h , max_w):
    image = Image.open(image) 
    
    if image.height < min_h :
        raise ValidationError(f'Image height must be at least {min_h}px')
    elif image.height > max_h : 
        raise ValidationError(f'Image height must be maximum {max_h}px')
    
    if image.width < min_w:
        raise ValidationError(f'Image width must be at least {min_w}px')
    elif image.width > max_w:
        raise ValidationError(f'Image width must be maximum {max_w}px')
    
    return image    

    
def update_field(self,request,pk ,data ,ErrorName , Error):
    try: 
    
        obj = get_object_or_404(self.serializer_class.Meta.model , pk=pk)
        data = data
        
        serializer = serializer_saver(serializer_class=self.get_serializer_class(),
                        instance = obj,
                        data=data,
                        context={"request":request},
                        partial=True)
        
    
    except Http404:
        return Response({"detail" : {f"{ErrorName}" : f"{Error}"}})
    except Exception as exc:
        return Response(exc.detail , status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data)


def get_related_field(self,serializer_class,related_name,ErrorName,Error,pk=None):
    try : 
        obj = get_object_or_404(self.serializer_class.Meta.model, pk=pk)
        obj = getattr(obj , related_name) 
        
    except Http404:
        return Response({"detail" : {f"{ErrorName}" : f"{Error}"}} , status=status.HTTP_404_NOT_FOUND)
    serializer = serializer_class(obj , many=True)

    return Response(serializer.data)