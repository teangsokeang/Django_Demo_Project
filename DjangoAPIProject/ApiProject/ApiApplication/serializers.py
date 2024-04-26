from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Book Id")
    title=serializers.CharField(label="Enter Book Title")
    author=serializers.CharField(label="Enter Author Names")

# api/serializers.py
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'dob'] # Specify fields you want to include in the API response
