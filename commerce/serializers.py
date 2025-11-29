from rest_framework import serializers
from .models import Product , ProductCategory , ProductStatus

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'

    

    def update(self, instance,validated_data):
        blocked_fields = ['product_user' , 'product_date']
        for data in validated_data.keys():
            if not data in blocked_fields:
                setattr(instance,data,validated_data[data])
        
        instance.save()

        return instance

