# INNER JOIN
select * from table_1 join table_2 ON table_1.col = table_2.col;
select
e.employeeNumber, e.firstName, e.lastName,
    c.customerName
from employees as e
inner join customers as c ON e.employeeNumber = c.salesRepEmployeeNumber;


# demonstrating in excel sheet ON
# JOIN
# group BY
# normalziation need
https://docs.google.com/spreadsheets/d/1nk__9mvZeo_pmoZW7_nK25BRJoTI4FDOA8hcGjnkBYc/edit?gid=0#gid=0


# demonstrating left join
select count(*) from products;
select count(*) from productLines;

insert into productLines values ('abcd', 'sfdg', NULL, NULL);

select * from productlines as p left join products as pl ON p.productLine = pl.productLine order by p.productLine;

