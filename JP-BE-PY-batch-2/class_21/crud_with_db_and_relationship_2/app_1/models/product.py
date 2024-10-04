from django.db import models

from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, related_name='category')
