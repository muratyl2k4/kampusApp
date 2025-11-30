from rest_framework import serializers
from .models import InternPlace , InternAnnouncement , InternCategory

class InternPlaceSerializer(serializers.ModelSerializer): 
    class Meta:
        model = InternPlace
        fields = '__all__'

class InternCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InternCategory
        fields = '__all__'
        
class InternAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternAnnouncement
        fields = '__all__'

        