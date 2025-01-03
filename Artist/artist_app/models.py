from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(blank=False,null=False)
    profile_pic = models.ImageField(upload_to="profile_pics",blank=False,null=False)
    security_answer = models.CharField(max_length=225)
    is_approved = models.BooleanField(default=True)
    
    def __str__(self):
        return f"This is the {self.user.username}'s Profile"
    