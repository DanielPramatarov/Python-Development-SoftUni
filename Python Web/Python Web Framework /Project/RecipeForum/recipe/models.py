from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
# Create your models here.
class Item(models.Model):
    dificult_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
)
 
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # user_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    item_name = models.CharField(max_length=200)
    item_desc = models.TextField()
    item_time_to_cook = models.IntegerField()
    item_image = models.CharField(max_length=500,default="")
    # //TODO  item_dificult 1-10 and remove default = 1  
    # item_dificult_level = models.IntegerField(choices=dificult_CHOICES)
    # //TODO  item_dificult 1-10 and remove default = 1    
    

    def __str__(self):
        return self.item_name
 

    def get_absolute_url(self):
        
           return reverse("recipe:detail", kwargs={"pk": self.pk})



