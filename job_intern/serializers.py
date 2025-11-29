from rest_framework import serializers
from .models import InternPlace , InternAnnouncement

class InternPlaceSerializer(serializers.ModelSerializer): 
    class Meta:
        model = InternPlace
        fields = '__all__'


class InternAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternAnnouncement
        fields = '__all__'

        