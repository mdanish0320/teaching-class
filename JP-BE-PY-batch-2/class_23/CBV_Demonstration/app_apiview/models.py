from django.db import models


# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
