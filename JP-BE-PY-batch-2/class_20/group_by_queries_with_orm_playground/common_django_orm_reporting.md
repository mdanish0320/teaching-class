
# Django ORM Equivalents for SQL GROUP BY Queries

Django ORM doesn't have a direct `GROUP BY` clause like SQL, but you can achieve the same results using the `annotate()` and `aggregate()` methods in combination with `values()` or `values_list()`.

## 1. Count the number of employees in each department

**SQL:**
```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

**Django ORM:**
```python
from django.db.models import Count

Employee.objects.values('department').annotate(employee_count=Count('id'))
```
- `values('department')`: Groups the results by department.
- `annotate(employee_count=Count('id'))`: Adds a count of the employees in each department.

---

## 2. Sum of sales per product

**SQL:**
```sql
SELECT product_id, SUM(sales_amount)
FROM sales
GROUP BY product_id;
```

**Django ORM:**
```python
from django.db.models import Sum

Sales.objects.values('product_id').annotate(total_sales=Sum('sales_amount'))
```
- `values('product_id')`: Groups the results by product_id.
- `annotate(total_sales=Sum('sales_amount'))`: Adds the total sales for each product.

---

## 3. Average salary by department

**SQL:**
```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

**Django ORM:**
```python
from django.db.models import Avg

Employee.objects.values('department').annotate(average_salary=Avg('salary'))
```
- `annotate(average_salary=Avg('salary'))`: Adds the average salary for each department.

---

## 4. Maximum and Minimum salaries by job title

**SQL:**
```sql
SELECT job_title, MAX(salary), MIN(salary)
FROM employees
GROUP BY job_title;
```

**Django ORM:**
```python
from django.db.models import Max, Min

Employee.objects.values('job_title').annotate(max_salary=Max('salary'), min_salary=Min('salary'))
```
- `annotate(max_salary=Max('salary'), min_salary=Min('salary'))`: Retrieves both maximum and minimum salary for each job_title.

---

## 5. Group by with HAVING (to filter groups)

**SQL:**
```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

**Django ORM:**
```python
from django.db.models import Count

Employee.objects.values('department').annotate(employee_count=Count('id')).filter(employee_count__gt=5)
```
- `filter(employee_count__gt=5)`: Filters departments with more than 5 employees.

---

## 6. Group by multiple columns (e.g., department and job title)

**SQL:**
```sql
SELECT department, job_title, COUNT(*)
FROM employees
GROUP BY department, job_title;
```

**Django ORM:**
```python
from django.db.models import Count

Employee.objects.values('department', 'job_title').annotate(employee_count=Count('id'))
```
- `values('department', 'job_title')`: Groups by both department and job_title.
- `annotate(employee_count=Count('id'))`: Counts the number of employees for each department and job title combination.

---

### Key Notes for Django ORM:
1. **`values()`**: Groups the results by the specified field(s).
2. **`annotate()`**: Adds an aggregate value (like `COUNT()`, `SUM()`, `AVG()`, etc.) to each group.
3. **`filter()`**: Can be used after `annotate()` to apply conditions like `HAVING` in SQL.

## Example with WHERE and HAVING

**SQL:**
```sql
SELECT department, COUNT(*)
FROM employees
WHERE is_active = 1
GROUP BY department
HAVING COUNT(*) > 5;
```

**Django ORM Equivalent:**
```python
from django.db.models import Count

Employee.objects.filter(is_active=True)     .values('department')     .annotate(employee_count=Count('id'))     .filter(employee_count__gt=5)
```
- The `filter(is_active=True)` part acts like the `WHERE` clause in SQL.
- The `.annotate(employee_count=Count('id'))` adds the count of employees for each department.
- The final `.filter(employee_count__gt=5)` is the equivalent of the `HAVING` clause, filtering groups that have more than 5 employees.

This way, you can apply both `WHERE` and `HAVING` conditions in Django ORM.
