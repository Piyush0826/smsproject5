from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class StudentList(models.Model):
    Register_Number = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def str(self):
        return self.Register_Number

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=10, null=True, blank=True)
    comments = models.TextField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.email})"

# models.py
from django.db import models

class ContactDetail(models.Model):
    objects = None
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=12)
    address = models.TextField()

    def __str__(self):
        return self.name
