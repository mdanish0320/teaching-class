# sub query / nested query

select * from employees;

select * from employees where (nested_query); # nested query 1
select * from (nested_query); # nested query 2
select *, (select * from employees) from employees; # nested query 3

# nested query 1, after where clause

select * from orderdetails;
select * from products;

-- select * from orderdetails where productCode = "S72_3212";
# get all orders related to the prodcuts "Pont Yacht"
select productcode from products where productname = "Pont Yacht";
select * from orderdetails where productcode = "S72_3212";

select * from orderdetails where productCode = (select productCode from products where productname = "Pont Yacht");

select * from orders order by customerNumber;


-- cat_name = "pont yacht"
-- f"select * from orderdetails where productCode = (select productCode from products where productname = {cat_name});"

# Get first order of every customer
select * from orders where customerNumber = 103;

select * from orders where orderDate = (
select min(orderDate) from orders where customerNumber = 112
) and customerNumber = 112;

select * from orders where orderDate = "2023-05-29";

select min(orderDate) from orders;

select min(orderDate), customerNumber from orders group by customerNumber;

select * from employees;

select * from offices;

select * from employees where officeCode = (select officeCode from offices where country = "USA");


select officeCode from offices where country = "USA";

select * from employees where officeCode IN (select officeCode from offices where country = "USA");

# sub query 2
select * from products order by buyPrice DESC;

select * from products order by buyPrice DESC limit 5;

select * from (
select * from products order by buyPrice DESC limit 5
) as t order by t.buyPrice ASC;



CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    salesperson_id INT,
    sale_amount DECIMAL(10, 2),
    sale_date DATE
);


INSERT INTO sales (salesperson_id, sale_amount, sale_date) VALUES
(1, 12000.00, '2024-08-01'),
(1, 8000.00, '2024-08-01'),
(1, 15000.00, '2024-08-02'),
(1, 11000.00, '2024-08-03'),
(2, 5000.00, '2024-08-01'),
(2, 12000.00, '2024-08-02'),
(2, 9000.00, '2024-08-02'),
(3, 10000.00, '2024-08-01'),
(3, 4000.00, '2024-08-03'),
(4, 8000.00, '2024-08-04'),
(4, 9000.00, '2024-08-04'),
(4, 7000.00, '2024-08-04');

select * from sales;

select avg(sale_amount) from sales;
select avg(sale_amount) from sales where salesperson_id = 1 group by sale_date;

select sum(sale_amount), sale_date from sales where salesperson_id = 1 group by sale_date;

select AVG(t.daily_avg)  from (
select sum(sale_amount) as daily_avg, sale_date from sales where salesperson_id = 1 group by sale_date
) as t ;


select AVG(t.daily_avg)  from (
select sum(sale_amount) as daily_avg, sale_date from sales where salesperson_id = 1 group by sale_date
) as t ;

select AVG(t.daily_avg) from (
select sum(sale_amount) as daily_avg, salesperson_id from sales  group by sale_date, salesperson_id
) as t group by salesperson_id;

# insert

select * from offices;
INSERT INTO TABLE_NAME () VALUES ();
INSERT INTO offices (
officeCode, city, phone, addressLine1, addressLine2,
state, country, postalCode, territory
) VALUES (1001, 'karachi', '123', 'xyz', 'abc', 'sindh', 'pakistan', '123', 'garden');

INSERT INTO TABLE_NAME VALUES ();
INSERT INTO offices VALUES (1002, 'karachi', '123', 'xyz', 'abc', 'sindh', 'pakistan', '123', 'garden');
INSERT INTO offices VALUES (1002, 'karachi', '123', 'xyz', 'abc', 'sindh', 'pakistan', '123', 'garden');
INSERT INTO offices VALUES (1002, 'karachi', '123', 'xyz', 'abc', 'sindh', 'pakistan', '123', 'garden');
INSERT INTO offices VALUES (1002, 'karachi', '123', 'xyz', 'abc', 'sindh', 'pakistan', '123', 'garden');
INSERT INTO offices VALUES (1002, 'karachi', '123', 'xyz', 'abc', 'sindh', 'pakistan', '123', 'garden');
INSERT INTO offices VALUES (1002, 'karachi', '123', 'xyz', 'abc', 'sindh', 'pakistan', '123', 'garden');


# update
SET SQL_SAFE_UPDATES = 0;
UPDATE offices SET city = "hyderabad" WHERE city = "karachi";

DELETE FROM TABLE WHERE COL_NAME = VALUE;


# CONSTRAINT
# NOT NULL
# UNIQUE
# FOREIGN KEY
# CASCADE
    # SET NULL
    # RESTRICT
    # NO ACTION
    # SET DEFAULT