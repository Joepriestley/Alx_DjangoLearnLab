from django.db import models
from django. contrib.auth.models  import AbstractUser
# Create your models here.

class UserCustom(AbstractUser):
    bio =models.CharField(max_length=225, null=True, blank=True)
    profile_picture =models.ImageField(upload_to="profile_img", null=True, blank=True)
    followers =models.ManyToManyField("self",symmetrical=False,null=True,blank=True)
    
    def __str__(self):
        return f"{self.username}"
    


