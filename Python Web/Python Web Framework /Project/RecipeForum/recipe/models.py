from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
# Create your models here.
class Item(models.Model):
 
 
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    item_name = models.CharField(max_length=200)
    item_desc = models.TextField()
    ingredients = models.CharField(max_length=250)
    item_time_to_cook = models.IntegerField()
    image = models.ImageField( upload_to="Recipes/") 
 
    

    def __str__(self):
        return self.item_name
 

    def get_absolute_url(self):
        
           return reverse("recipe:detail", kwargs={"pk": self.pk})



