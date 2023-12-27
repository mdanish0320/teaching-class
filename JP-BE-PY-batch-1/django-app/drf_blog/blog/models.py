from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AuthorModel(models.Model):
  fname = models.CharField(max_length=200)
  lname = models.CharField(max_length=200)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.fname +" "+ self.lname
  

class PostModel(models.Model):
  title = models.CharField(max_length=200)
  desc = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True) # add datetime only once the record is created
  updated_at = models.DateTimeField(auto_now=True) # updates datetime on every change