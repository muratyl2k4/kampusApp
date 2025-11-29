from rest_framework import serializers
from .models import DiscountAnnouncement

class DiscountAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountAnnouncement
        fields = '__all__'