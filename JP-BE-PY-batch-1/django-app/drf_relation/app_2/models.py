from django.db import models

# Create your models here.

class Employee(models.Model):
  name = models.CharField(max_length=200)

class Project(models.Model):
  title = models.CharField(max_length=200)
  employee = models.ManyToManyField(Employee, through='EmployeeProjectAssignment')
  
class EmployeeProjectAssignment(models.Model):
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  assignment_date = models.DateField()
  is_active = models.BooleanField()
  created_at = models.DateTimeField(auto_now_add=True) # first time
  updated_at = models.DateTimeField(auto_now=True) # every time when model.save runs
  

