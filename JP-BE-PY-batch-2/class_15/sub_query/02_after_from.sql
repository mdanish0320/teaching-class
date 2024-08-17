# nested query 2, after from clause

# example 1: Get five highest prices products. But display it in reverse order (lowest to highest)

select * from products order by buyPrice DESC;
select * from products order by buyPrice DESC limit 5;

select * from (
  select * from products order by buyPrice DESC limit 5
) as t order by t.buyPrice ASC;

# example 2:
# calculate daily average sale of the person
# and also who have made sales on more than one day and, on those days, their total daily sales exceed $10,000 on average.


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

# explanantion break down queries
select * from sales;

# whole company average sale
select avg(sale_amount) from sales; 

# per day average sale of company
select avg(sale_amount) from sales group by sale_date; 

# employee_1 overall average sale
select avg(sale_amount) from sales where salesperson_id = 1 group by salesperson_id; 

# wrong
# employee_1 per day average sale
# we cannot achieve daily sale by only 1 query
select avg(sale_amount) from sales where salesperson_id = 1 group by sale_date; 

# correct nested query for employee_1
# calculate daily average sale of one employee
select sum(sale_amount) from sales where salesperson_id = 1 group by sale_date;
select AVG(t.daily_avg)  from (
  select sum(sale_amount) as daily_avg, sale_date from sales where salesperson_id = 1 group by sale_date
) as t ;

# calculate daily average sale of every employee
select AVG(t.daily_avg) from (
  select sum(sale_amount) as daily_avg, salesperson_id from sales  group by sale_date, salesperson_id
) as t group by salesperson_id;