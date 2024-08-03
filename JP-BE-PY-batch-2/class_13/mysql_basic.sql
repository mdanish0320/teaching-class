# command to select database
USE classicmodels;

# display all columns and all rows of specific table that exists in the database classicmodels
SELECT * FROM employees;
SELECT * FROM products;
SELECT * FROM orders;


# NOTE:
# must add semicolon at the end of each query
# Query keywords are case in-sensitive


# display whole data of only 2 columns of table "employees"
SELECT firstName, lastName FROM employees;

## LIMIT
# display only 2 rows and 2 columns of the table "employees"
SELECT firstName, lastName FROM employee LIMIT 2;

## SORT
# display all employees and also sort it by employee name (A-Z)
SELECT firstName, lastName FROM employee ORDER BY firstName, lastName;
# display all employees and also sort it by employee name in reverse alphabatical order (Z-A)
SELECT firstName, lastName FROM employee ORDER BY firstName DESC, lastName DESC;
# display all employee and sort it by employee number
SELECT firstName, lastName FROM employee ORDER BY employeeNumber;

## OFFSET
# display whole employee data and sort it by Name and only display first 5 rows
SELECT * FROM employees ORDER BY firstName, lastName LIMIT 5
# display whole employee data and sort it by Name and display next 5 rows
SELECT * FROM employees ORDER BY firstName, lastName LIMIT 5 OFFSET 5
# display whole employee data and sort it by Name and display further next 5 rows
SELECT * FROM employees ORDER BY firstName, lastName LIMIT 5 OFFSET 10
# display whole employee data and sort it by Name and display further next 5 rows
SELECT * FROM employees ORDER BY firstName, lastName LIMIT 5 OFFSET 15

# display the third employee (only 1 row) from the list when the list is sorted by employee name
SELECT * FROM employees ORDER BY firstName, lastName LIMIT 1 OFFSET 2

# ALIAS
# rename the column name from firstName to fname and lastName to last_name while fetching the data from employee table
SELECT 
  firstName as fname, 
  lastName as last_name 
FROM 
  employees