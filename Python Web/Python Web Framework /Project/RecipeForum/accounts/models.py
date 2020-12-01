from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    #//TODO makemigrations and migrate
    firstname = models.CharField(max_length=255, null=True)
    info = models.TextField(max_length=500, null=True)
    lastname = models.CharField(max_length=255, null=True)
    data_of_birth = models.DateTimeField(null=True)
    profile_image = models.ImageField( upload_to="profiles/") 
    Phone_number = models.CharField(max_length=200, null=True)
    Email = models.EmailField(max_length=200, null=True)
    adress = models.CharField(max_length=200, null=True)
    facebook_url = models.CharField(max_length=200, null=True)
    instagram_url = models.CharField(max_length=200, null=True)
    twitter_url = models.CharField(max_length=200, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


