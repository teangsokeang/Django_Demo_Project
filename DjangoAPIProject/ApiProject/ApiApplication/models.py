from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

default_value = timezone.now

# Create your models here.
class Book(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

# models.py



# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)  # Add email field

#     USERNAME_FIELD = 'email'  # Use email as the username field
#     REQUIRED_FIELDS = []     # We don't require any additional fields for registration

#     # Specify custom related_name attributes for groups and user_permissions
#     groups = models.ManyToManyField(
#         'auth.Group',
#         verbose_name='groups',
#         blank=True,
#         related_name='custom_users',  # Custom related_name
#         related_query_name='user',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         verbose_name='user permissions',
#         blank=True,
#         related_name='custom_users_permissions',  # Custom related_name
#         related_query_name='user',
#     )
