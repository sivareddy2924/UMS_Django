from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class UserDetail(models.Model):
    auth_user = models.ForeignKey(User, related_name='auth_user', on_delete=models.CASCADE)
    fname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
class Course(models.Model):
    # Basic fields for the course
    course_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    
    # Optional: You can include a foreign key to a department or instructor if needed
    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)

    # Dates for course start and end
    start_date = models.DateField()
    end_date = models.DateField()

    # Method to return a string representation of the course
    def __str__(self):
        return f"{self.course_code} - {self.course_name}"

class Instructor(models.Model):
    # Simple instructor model with name and email for demonstration
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Department(models.Model):
    # Department model for categorizing courses
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name