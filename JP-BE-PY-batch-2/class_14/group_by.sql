# functions
MIN(), Max(), AVG(), COUNT(),  SUM()

select * from payments;
#
select MAX(amount) from payments where YEAR(paymentDAte) = 2003;
select MAX(amount) from payments where YEAR(paymentDAte) = 2004;
select MAX(amount) from payments where YEAR(paymentDAte) = 2005;

select max(amount), Year(paymentDate) from payments group by YEAR(paymentDate);

Select Distinct( YEAR(paymentDate)) from payments;

Select YEAR(paymentDate) from payments group by YEAR(paymentDate) ;


select max(amount) as max_amount, Year(paymentDate) from payments group by YEAR(paymentDate) HAVING max_amount > 116208;

select max(amount) as max_amount, Year(paymentDate) from payments WHERE max_amount > 116208;



select
max(amount) as max_amount,
    Year(paymentDate)
from payments
group by YEAR(paymentDate);
   
   
select
max(amount) as max_amount,
    Year(paymentDate)
from payments
where  Year(paymentDate) != 2004
group by YEAR(paymentDate)
    HAVING YEAR(paymentDate) > 2003;
   
   
select * from customers;

select count(*) from customers; # 112

select distinct city from customers;
select count(distinct city) from customers; # 95


select * from customers where city = "Nantes";
select count(city) from customers where city = "Nantes";

select count(*), country from customers group by country;

select * from customers;

# query execution order

# from
# where
# group by
# having
# SELECT
# order by 
# limit

select count(*), salesRepEmployeeNumber from customers group by salesRepEmployeeNumber;

select salesRepEmployeeNumber,  max(creditLimit)  from customers group by salesRepEmployeeNumber;

select count(*), salesRepEmployeeNumber as emp_id from customers group by salesRepEmployeeNumber having emp_id is not null;

select max(creditLimit), sum(creditLimit), city from customers group by city;