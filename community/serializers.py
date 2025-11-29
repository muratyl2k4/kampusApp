from rest_framework import serializers
from .models import Community , CommunityAnnouncement

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'



class CommunityAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityAnnouncement
        fields = '__all__'

    def update(self, instance, validated_data):
        blocked_fields = ['announcement_community']
        for key in validated_data.keys():
            if not key in blocked_fields:
                setattr(instance , key , validated_data[key])
        instance.save()

        return instance
