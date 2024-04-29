from rest_framework import serializers
from .models import *

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Book Id")
    title=serializers.CharField(label="Enter Book Title")
    author=serializers.CharField(label="Enter Author Names")

# api/serializers.py

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'dob'] # Specify fields you want to include in the API response

# serializers.py

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password']  # Add other fields as needed
#         extra_kwargs = {'password': {'write_only': True}}

