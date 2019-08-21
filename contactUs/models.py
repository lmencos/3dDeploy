from django.db import models

# Create your models here.
class ContactUs(models.Model):
  firstName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=20)
  email = models.EmailField(max_length=30, unique=True)
  twitter = models.CharField(max_length=30, unique=True)
  message = models.CharField(max_length=500, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)