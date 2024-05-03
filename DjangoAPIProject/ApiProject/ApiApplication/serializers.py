from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer): 
    # class Meta: 
    #     model = User 
    #     fields = ['username', 'password']
    # def create(self, validated_data): 
    #     user = User.objects.create(username=validated_data['username'])
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)



class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Book Id")
    title=serializers.CharField(label="Enter Book Title")
    author=serializers.CharField(label="Enter Author Names")

# api/serializers.py

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'sex', 'dob', 'address', 'phone_number', 'email', 'major'] # Specify fields you want to include in the API response

# serializers.py

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password']  # Add other fields as needed
#         extra_kwargs = {'password': {'write_only': True}}

