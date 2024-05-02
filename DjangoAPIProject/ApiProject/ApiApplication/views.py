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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .serializers import UserSerializer

@method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF protection for this view
class LoginAPIView(APIView):
    # serializer_class = UserSerializer
    # def get(self, request):
    #     # This is just an example. You can customize the GET method as needed.
    #     users = User.objects.all()
    #     serializer = self.serializer_class(users, many=True)
    #     return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserRegistration(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        # This is just an example. You can customize the GET method as needed.
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            token = Token.objects.create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


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
    
    
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to create, update, or delete students.
    """
    def has_permission(self, request, view):
        # Read-only permissions are allowed for anyone, so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow admins to create, update, or delete students.
        if request.user and request.user.is_staff:
            return True
        else:
            # If the user doesn't have permission, return a custom error response
            return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    

class StudentAPIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

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
    

