from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")



# Create your models here.
class Categoryy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Productt(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Categoryy, related_name="categoryy")