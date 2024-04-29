from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token


# Create your views here.
class BookApiView(APIView):
    serializer_class=BookSerializer
    def get(self,request):
        allBooks=Book.objects.all().values()
        return Response({"Message":"List of Books", "Book List":allBooks})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=BookSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Book.objects.create(id=serializer_obj.data.get("id"),
                            title=serializer_obj.data.get("title"),
                            author=serializer_obj.data.get("author")
                            )

        book=Book.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Book Added!", "Book":book})
    
class StudentAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        try:
            return Student.objects.get(pk=id)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ApiApplication/views.py


class StudentDetailView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# views.py


# class UserRegistrationAPIView(generics.CreateAPIView):
#     serializer_class = UserSerializer

# class UserLoginAPIView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = CustomUser.objects.get(username=username)
#         if user.check_password(password):
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         else:
#             return Response({'error': 'Invalid credentials'}, status=400)

# class UserProfileAPIView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)

    

