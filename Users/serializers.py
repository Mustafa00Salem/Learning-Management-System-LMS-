from rest_framework import serializers
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',  'email','password', 'role', 'profile_picture']
        extra_kwargs = {
            "password":{"write_only":True, },
            'email': {'required': False},
            'profile_picture': {'required': False},
            
            }
        
    def validate_password(self,value):
        if len(value) < 8 :
            raise serializers.ValidationError("Minimum 8 characters")
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError(
                "Password must contain an uppercase letter."
            )

        if not re.search(r"[a-z]", value):
            raise serializers.ValidationError(
                "Password must contain a lowercase letter."
            )
        return value
        
    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["email"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            role=validated_data.get("role"),
            profile_picture=validated_data.get("profile_picture"),
        )
    

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name','last_name', 'email', 'role','profile_picture']
        
        read_only_fields = (
            "id",
            "role",
        )
        
        
class ChangePasswordSerializers(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate_new_password(self, value):

        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters."
            )

        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError(
                "Password must contain an uppercase letter."
            )

        if not re.search(r"[a-z]", value):
            raise serializers.ValidationError(
                "Password must contain a lowercase letter."
            )
        return value


    def validate(self, attrs):

        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )

        return attrs
    
class LogoutSerilaizer(serializers.Serializer):
    refresh = serializers.CharField()