from django.db import models
from django.contrib.auth.models import User
from app.models import Category


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
