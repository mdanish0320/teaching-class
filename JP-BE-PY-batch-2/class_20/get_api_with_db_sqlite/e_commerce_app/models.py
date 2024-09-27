from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.FloatField()
    cat_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
