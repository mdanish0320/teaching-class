# nested query 1, after where clause

select * from orderdetails;
select * from products;

# explanation: https://docs.google.com/spreadsheets/d/1nk__9mvZeo_pmoZW7_nK25BRJoTI4FDOA8hcGjnkBYc/edit?gid=1763420898#gid=1763420898

# example 1: get all orders related to the prodcuts "Pont Yacht" - manually
select productcode from products where productname = "Pont Yacht";
select * from orderdetails where productcode = "S72_3212";

# by sub query
select * from orderdetails where productCode = (select productCode from products where productname = "Pont Yacht");


# # example 2: Get first order of one customer by order_date
select * from orders where customerNumber = 112;

select * from orders where orderDate = (
  select min(orderDate) from orders where customerNumber = 112
) and customerNumber = 112;

# Get latest order of every customer by id
select * from orders where orderNumber IN (
  select max(orderNumber) from orders group by customerNumber
);


# explanation
select * from orders where orderDate = "2023-05-29";
select min(orderDate) from orders;
select min(orderDate), customerNumber from orders group by customerNumber;

# class task
# Display all employees who are working in USA country (classicmodels)
select * from employees;
select * from offices;

# error
select * from employees where officeCode = (select officeCode from offices where country = "USA");
select officeCode from offices where country = "USA";
select * from employees where officeCode IN (select officeCode from offices where country = "USA");
