from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class StudentProfile(models.Model):
    OAPR = models.FloatField()
    SHS_Strand = models.CharField(max_length=100)  # You can adjust the max_length as needed
    SHS_GWA = models.FloatField()
    recommended_course = models.CharField(max_length=100)  # You can adjust the max_length as needed

    def __str__(self):
        return f"Student: {self.id}, Recommended Course: {self.recommended_course}"

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()
    
    def __str__ (self):
        return self.username
    
class Account(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)

    cet = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    shs_track = models.CharField(max_length=255, blank=True, null=True)
    shs_gpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class PredResults(models.Model):

    cet = models.FloatField()
    gpa = models.FloatField()
    strand = models.CharField(max_length=200)
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification
