USE classicmodels;

SELECT * FROM employees;

SELECT * FROM classicmodels.employees;

select * FROM employees LIMIT 5;
select * FROM employees LIMIT 2;

select * FROM employees ORDER BY firstName LIMIT 2;
select * FROM employees ORDER BY firstName ASC;
select * FROM employees ORDER BY firstName DESC;

select * FROM employees ORDER BY firstName DESC LIMIT 2;

# fetch all columns and all rows
# fetch only 2 rows
# fetch data by sorting ASC/desc
# alias
# fetch few columns
# order by multiple columns

select firstname, LASTNAME from employees;

select firstname AS fname, LASTNAME as lname from employees;


select * from employees LIMIT 5;
select * from employees LIMIT 10 OFFSET 0;
select * from employees LIMIT 10 OFFSET 10;
select * from employees LIMIT 10 OFFSET 20;
select * from employees LIMIT 10 OFFSET 30;







SELECT * FROM products;

SELECT * FROM products order by productLine ASC limit 2 ;

SELECT * FROM products order by productVendor DESC ;


select * from employees order by firstName;

select * from employees order by firstName ASC, lastname ASC;

select * from employees order by jobTitle, firstName;
insert into employees values ('1002000', 'Zzzz', 'Abdullah', 'x5800', 'abdullah@classicmodelcars.com', '1', NULL, 'President');
 

select * from employees WHERE email = "abdullah@classicmodelcars.com";
select * from employees WHERE email = "abdullah@classicodelcars.com";

select * from employees order by jobtitle;

select * from employees where jobtitle like "Sale% Manager%";

select * from employees where reportsTo IS NULL;



select * from employees where jobtitle = "Sales Rep";
select * from employees where jobtitle = "Sales Rep" AND reportsTo = "1143";
select * from employees where jobtitle = "Sales Rep" OR reportsTo = "1143";


update employees set reportsTo = 1143 where employeeNumber = 1102;



select
*
from
employees
where
jobtitle = "Sales Rep"
    AND reportsTo = "1143"
    AND officeCode != 1
    ;
   
select
*
from
employees
where
jobtitle = "Sales Rep"
    AND reportsTo = "1143"
    AND (officeCode = 2 OR officeCode = 3)
    ;
   
select
*
from
employees
where
jobtitle = "Sales Rep"
    AND reportsTo = "1143"
    AND officeCode IN (2, 3)
    ;
   
Select * from orders;

# 2003-01-06

select * from orders where orderDate = "2003-01-06";

select * from orders where MONTH(orderDate) = 1;

select * from orders where MONTH(orderDate) = 1 AND YEAR(orderDate) = 2003;

select * from orderdetails;

select MAX(quantityOrdered) from orderdetails;

select * from payments;

select amount from payments where YEAR(paymentDate) = 2003;

select MAX(amount) from payments where YEAR(paymentDate) = 2003;
select MIN(amount) from payments where YEAR(paymentDate) = 2003;


select MAX(amount) from payments;

select MAX(amount) from payments where YEAR(paymentDAte) = 2003;
select MAX(amount) from payments where YEAR(paymentDAte) = 2004;
select MAX(amount) from payments where YEAR(paymentDAte) = 2005;
select MAX(amount) from payments where YEAR(paymentDAte) = 2006;

select *, MAX(amount) from payments where YEAR(paymentDAte) = 2003;

select * from payments where YEAR(paymentDAte) = 2003;