from django.db import models

# Define the models corresponding to the SQLite database tables
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    salary = models.FloatField()
    is_active = models.BooleanField()

    class Meta:
        db_table = 'employees'
        managed = False  # We don't want Django to manage the table

class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    sales_amount = models.FloatField()

    class Meta:
        db_table = 'sales'
        managed = False  # We don't want Django to manage the table
