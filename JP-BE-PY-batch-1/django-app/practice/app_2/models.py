from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    name = models.CharField(max_length=200)



class EmployeeModel(models.Model):
    name = models.CharField(max_length=200)
    departments = models.ManyToManyField(DepartmentModel)


class SalaryModel(models.Model):
    salary_date = models.DateField()
    employee_id = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
