## SUB QUERY (NESTED QUERY)

# sub query that can be written in WHERE clause
SELECT * FROM products WHERE buyPrice > (SELECT AVG(buyPrice) FROM products);


# sub query that can be used as table
select * from (
  SELECT buyPrice FROM products order by buyPrice DESC limit 5
) as t order by buyPrice ASC;

# sub query that can fetch values from other table in column level
# ....


# class task: get all employees that have successfully captured a customer
SELECT * FROM employees WHERE employeeNumber IN (
  SELECT salesRepEmployeeNumber from customers
);





