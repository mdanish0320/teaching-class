## SUB QUERY (NESTED QUERY)

# sub query that can be written in WHERE clause
SELECT * FROM products WHERE buyPrice > (SELECT AVG(buyPrice) FROM products);


# sub query that can be used as table
select * from (
  SELECT buyPrice FROM products order by buyPrice DESC limit 5
) as t order by buyPrice ASC;

# sub query that can fetch values from other (or same) table in column level
# fetch all employees name and their manager name from same table `employees`
SELECT 
	employeeNumber,
	firstName, 
    lastName, 
	(
		SELECT 
      concat( 
            firstName,
            lastName
      ) 
    FROM employees as manager where emp1.reportsTo = manager.reportsTo limit 1
  ) as manager_name,
    reportsTo as manager_id
FROM 
	employees emp1;


# class task: get all employees that have successfully captured a customer
SELECT * FROM employees WHERE employeeNumber IN (
  SELECT salesRepEmployeeNumber from customers
);





