from django.db import models


# Create your models here.
class Person(models.Model):
  name = models.CharField(max_length=200)
  age = models.IntegerField()