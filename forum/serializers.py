from rest_framework import serializers
from .models import Entry , EntryComment , EntryLike ,Topic

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields= '__all__'


class EntrySerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Entry
        fields = '__all__'

class EntryLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntryLike
        fields='__all__'

    def update(self,instance,validated_data):

        return instance

    



class EntryCommentSerializer(serializers.ModelSerializer):

    class Meta :
        model = EntryComment
        fields = '__all__'

