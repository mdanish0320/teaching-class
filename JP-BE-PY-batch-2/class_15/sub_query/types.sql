select * from employees where (nested_query); # nested query 1

select * from (nested_query); # nested query 2

select *, (select * from employees) from employees; # nested query 3
