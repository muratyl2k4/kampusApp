from rest_framework import serializers 
from .models import KampusUser
from PIL import Image
from django.core.exceptions import ValidationError
from core.helpers import validate_image
class ProfilePictureValidationSerializer(serializers.ModelSerializer):
    def validate_Profile_Picture(self,value):
        
        value = validate_image(image=value , min_h=500,max_h=1000,min_w=500,max_w=1000)
        return value

class UserSerializer(ProfilePictureValidationSerializer):

    class Meta:
        model = KampusUser
        fields = ['Username' , 'first_name' , 'last_name' ,'email', 'StudentID' ,'Profile_Picture' ,'password' ,'Role']
        extra_kwargs = {"password" : {"error_messages" : {"required" : "Password required"}},
                        "StudentID" : {"error_messages" : {"required" : "Student ID is required"}},
                        "Username" : {"error_messages" : {"required" : "Username is required"}},
                        "Role" : {"error_messages" : {"required" : "Role is required" } }
                        }
        
    def create(self, validated_data):
        user = KampusUser(

            #required fields
            # first_name = validated_data['first_name'],
            # last_name = validated_data['last_name'], 
            # Username = validated_data['Username'] , 
            # Role = 'Student',
            # StudentID = validated_data['StudentID']
        )
        for key in self.get_fields():
            if not key=='password':
                user[key] = validated_data[key]

        
        user.set_password(validated_data['password'])
        
        user.save()
        return user

    def validate_Role(self,value):
        rolelist= [choice[0] for choice in self.Meta.model.rolelist]

        if not value in rolelist:
            raise serializers.ValidationError(f"{value} is not a Role")
        return value
    
        
    
class MeSerializer(ProfilePictureValidationSerializer):
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = KampusUser
        fields = ["Username", "first_name" , "last_name" , "email" , "password" ,'Profile_Picture','Phone_Number' , 'Role']
        read_only_fields = ['Role']
    

    def update(self, instance, validated_data):
        if "Username" in validated_data:
            instance.Username = validated_data["Username"]
        if "password" in validated_data:
            instance.set_password(validated_data["password"])
        if 'Profile_Picture' in validated_data:
            instance.Profile_Picture = validated_data['Profile_Picture']
        if 'Phone_Number' in validated_data:
            instance.Phone_Number = validated_data['Phone_Number']
        instance.save()
        return instance
