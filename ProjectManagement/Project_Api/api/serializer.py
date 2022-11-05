
from dataclasses import fields
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Project,Task,Permissions,UserProjectPermission

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length = 8,
        required = True,
        error_messages = {
            "min_length":"password must be minimum 8 length"
        },
        style={'input_type': 'password', 'placeholder': ' Re-Password'}
    )
    email = serializers.EmailField()

    password2 = serializers.CharField(
        write_only=True,
        min_length = 8,
        required = True,
        error_messages = {
            "min_length":"password must be minimum 8 length"
        },
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['id','username','email','password','password2'] #yaha vahi field jo create k time dalna ho table m

    def validate(self, data):
        if data['password'] != data["password2"]:
            raise serializers.ValidationError("password must be same")
        return data
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"],
            email = validated_data["email"],    
                  
        )

        user.set_password(validated_data["password"])
        user.save()

        return user

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields= "__all__"
    
    def get_count(self,obj):
        # Provided the user is logged:
        user_id = self.context['request'].user.id
        # Now do whatever with user_id
        return

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = "__all__"

class UserProjectPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProjectPermission
        fields = "__all__"