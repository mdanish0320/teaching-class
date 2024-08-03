## WHERE
# filter rows based on one column
SELECT * FROM employees where email = "abow@classicmodelcars.com";

# filter rows based on multiple columns using AND Clasue (it will return the rows if both condition matches in same row)
SELECT * FROM employees where firstName = "Anthony" AND lastName = "Bow";

# filter rows based on multiple columns using OR Clause
SELECT * FROM employees where firstName = "Peter" OR firstName = "Anthony";
SELECT * FROM employees where firstName IN ("Peter", "Anthony");

# combination of AND and OR
SELECT * FROM employees where (firstName = "Peter" OR firstName = "Anthony") AND (reportsTo = 1088);

# Fetch rows based on NULL values
select * from employees where reportsTo IS NULL;

# Fetch data based on range condition
select * from employees where officeCode BETWEEN 1 AND 5;

# INVERSE CONDITIONS
SELECT * FROM employees where email != "abow@classicmodelcars.com";
SELECT * FROM employees where firstName NOT IN ("Peter", "Anthony");
select * from employees where reportsTo IS NOT NULL;
select * from employees where officeCode NOT BETWEEN 1 AND 5;

# SUB STRING SEARCH USING LIKE CLAUSE
SELECT * FROM customers where customerName like "%Mini%";
SELECT * FROM customers where customerName like "Mini%";
SELECT * FROM customers where customerName like "%Mini";
SELECT * FROM customers where customerName like "Mini%Ltd.";