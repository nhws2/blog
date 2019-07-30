from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True)
    created_at = models.DateField(auto_now_add= True)
    updated_at = models.DateField(auto_now = True)
    category = models.CharField(max_length= 50,blank=True)
