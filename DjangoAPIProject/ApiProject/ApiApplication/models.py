from django.db import models
from datetime import datetime
from django.utils import timezone

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