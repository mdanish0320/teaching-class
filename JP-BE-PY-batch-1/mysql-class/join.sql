# fetch movie_title and langugae using sub-query
SELECT
f.title,
(SELECT name from language as l WHERE  f.language_id = l.language_id)
FROM
film as f;


# fetch actor name and film name using sub-query
SELECT
(SELECT first_name from actor as a WHERE  a.actor_id = fa.actor_id),
    (SELECT title from film as f WHERE  f.film_id = fa.film_id)
FROM
film_actor as fa;
   

# JOIN SYNTAX
SELECT
  *
FROM
TABLE_1
JOIN TABLE_2 ON TABLE_1.ID = TABLE_2.TABLE_1_ID;

# fetch movie_title and langugae using JOIN
SELECT
f.title,
    l.name,
    f.last_update as film_last_update,
    l.last_update as lang_last_update
FROM
film AS f
INNER JOIN language as l ON f.language_id = l.language_id;

# fetch film name and actor name using JOIN
SELECT
f.title,
    a.first_name
FROM
  film AS f
INNER JOIN film_actor as fa ON f.film_id = fa.film_id
INNER JOIN actor as a ON a.actor_id = fa.actor_id;
   
# LEFT/RIGHT JOIN
# find all employees who captures customers
use classicmodels;
SET foreign_key_checks = 0;
DELETE FROM classicmodels.customers WHERE customerNumber NOT IN (103, 112, 114, 119, 121);
select 
	emp.firstName, 
	emp.lastName,
	cus.customerName
FROM 
	employees emp
INNER JOIN customers cus ON  emp.employeeNumber = cus.salesRepEmployeeNumber;;

# find all employees who captures OR NOT CAPTURES customers
use classicmodels;
SET foreign_key_checks = 0;
DELETE FROM classicmodels.customers WHERE customerNumber NOT IN (103, 112, 114, 119, 121);
select 
	emp.firstName, 
	emp.lastName,
	cus.customerName
FROM 
	employees emp
LEFT JOIN customers cus ON  emp.employeeNumber = cus.salesRepEmployeeNumber;;


# fetch all city and country name
