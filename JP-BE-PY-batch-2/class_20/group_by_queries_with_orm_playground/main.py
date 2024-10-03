
import os

import django
from django.db import models

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from app.models import Employee, Sale




# Query 1: COUNT of employees grouped by department
departments_count = Employee.objects.values('department').annotate(count=models.Count('id'))
print("Employees count by department:")
for dept in departments_count:
    print(dept)

# Query 2: SUM of sales amount grouped by product_id
products_sales_sum = Sale.objects.values('product_id').annotate(total_sales=models.Sum('sales_amount'))
print("\nTotal sales amount by product:")
for product in products_sales_sum:
    print(product)

# Query 3: AVG salary grouped by department
avg_salary_by_department = Employee.objects.values('department').annotate(avg_salary=models.Avg('salary'))
print("\nAverage salary by department:")
for dept in avg_salary_by_department:
    print(dept)

# Query 4: MAX and MIN salary by job title
salary_range_by_job_title = Employee.objects.values('job_title').annotate(
    max_salary=models.Max('salary'),
    min_salary=models.Min('salary')
)
print("\nSalary range by job title:")
for job in salary_range_by_job_title:
    print(job)

# Query 5: Departments with more than 5 employees
departments_with_more_than_5 = Employee.objects.values('department').annotate(count=models.Count('id')).filter(count__gt=5)
print("\nDepartments with more than 5 employees:")
for dept in departments_with_more_than_5:
    print(dept)

# Query 6: COUNT of employees grouped by department and job title
departments_job_title_count = Employee.objects.values('department', 'job_title').annotate(count=models.Count('id'))
print("\nEmployees count by department and job title:")
for dept_job in departments_job_title_count:
    print(dept_job)

# Query 7: Active employees grouped by department with more than 5 employees
active_departments_with_more_than_5 = Employee.objects.filter(is_active=True).values('department').annotate(count=models.Count('id')).filter(count__gt=5)
print("\nActive departments with more than 5 employees:")
for dept in active_departments_with_more_than_5:
    print(dept)
