from django.db import models

# Create your models here.
class AuthorModel(models.Model):
  fname = models.CharField(max_length=200)
  lname = models.CharField(max_length=200)
  
  def __str__(self):
    return self.fname +" "+ self.lname
  

class PostModel(models.Model):
  title = models.CharField(max_length=200)
  desc = models.TextField()
  author_id = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)