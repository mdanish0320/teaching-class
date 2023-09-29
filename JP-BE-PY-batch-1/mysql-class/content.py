# install mysql workbench
    # https://www.youtube.com/watch?v=2om3byn2lxs
    # https://www.youtube.com/watch?v=GwHpIl0vqY4
# connect to database
# import db file
# data stroed in db is much like spread sheet
# relational database
# case insensitive command
# semicolon 

# RDBMS
    # Mysql - open sourced
    # Sql Server
    # Oracle
    # SQLite
    # PostgreSQL
    # MariaDB
    # etc

# Topics
# Use Database
# Select * from table
    # select * from customers;
    # select * from products;
    # select * from orders;
# Select few columns from table
# LIMIT: select * from table limit 10
# ORDER BY: select * from table order by name ASC or DESC
# OFFSET: it means start retrive the data AFTER the mentioned number
# column alias


# WHERE
    # single and multiple condition
    # And # # select * from customers where country = "USA" and city = "NYC";
    # or # select * from customers where city = "NYC" OR city = "Brickhaven";
    # != (not equal to)
    # IN, NOT IN
    # is null, not null
    # like
    # between
    # date comparison

# sub queries
    # placement inside
        # select clause
        # from clause
        # where clause
        # Correlated subqueries  are slower as it run for each row
    # select * ( select AVG(salary) from table ) from table
    # select * from table where salary > ( select salary from table )
    # to select data based on other table like join i.e IN Clause
    # display last 5 rows without changing the order
        # SELECT * FROM (SELECT * FROM actor ORDER BY actor_id DESC LIMIT 10) as t1 ORDER BY actor_id ASC;
    # select t1.col1, t1.col2, (select name from clinics where id = t1.clinic_id) from table t1
    # types: https://www.scaler.com/topics/sql/types-of-subqueries-in-sql/

# Group By
    # having
    # https://www.youtube.com/watch?v=FztbYXeOEQ4
    # https://www.youtube.com/watch?v=fR5rxzqEv7o
    # https://www.youtube.com/watch?v=SvJLXj05cow
    # https://www.youtube.com/watch?v=Se2RAkEc944
    # https://www.youtube.com/watch?v=VJZpPgxd3zw

# difference between where and having
"""
A HAVING clause is like a WHERE clause, but applies only to groups as a whole (that is, to the rows in the result set representing groups), whereas the WHERE clause applies to individual rows. A query can contain both a WHERE clause and a HAVING clause. In that case:

The WHERE clause is applied first to the individual rows in the tables or table-valued objects in the Diagram pane. Only the rows that meet the conditions in the WHERE clause are grouped.

The HAVING clause is then applied to the rows in the result set. Only the groups that meet the HAVING conditions appear in the query output. You can apply a HAVING clause only to columns that also appear in the GROUP BY clause or in an aggregate function.
"""


# function
    # distinct
    # concat, group_concat
    # lower case, upper case
    # Year(), MONTH(), DAY(), DATE()
    # Date_subtract() https://www.w3schools.com/sql/func_mysql_date_sub.asp
    # DATE_ADD() https://www.w3schools.com/sql/func_mysql_date_add.asp
    # https://www.w3schools.com/mysql/mysql_ref_functions.asp


# JOIN
    # inner join
    # left join
    # right join
    # outer join
    # cross join
    # multiple join
    # relationship: one-to-many etc


# INSERT
    # insert into table_name values(1,2,3)
    # insert into table_name (col1, col2, col3) values(1,2,3)
    # MULTI INSERT
    # insert into table_name values (1,2,3), (4,5,6), (7,8,9)
    # SHOW VARIABLES LIKE 'max_allowed_packet'; bytes
    # INSERT INTO table2 SELECT * FROM table1; no impact of max_allowed_packet

# update table
# delete from table

# https://www.youtube.com/watch?v=xipnW2w5EfE
# https://www.youtube.com/watch?v=7S_tz1z_5bA


# datatype
    # numeric, int, float
    # string (char vs varchar), text
    # datetime
    # blob
    # json

# Table level queries
    # # table name singular or plural
    # column name singular or plural

# constraint
    # NOT NULL
    # primary key
    # Foreign Key
    # unique
    # Check

# is auto increment field is a constraint?

# Arithmatic Operation i.e addition and subtraction

# main components
# - DDL -> table level - create, alter, drop
# - DML -> data level - select, insert, update, delete
# - DCL -> Grant 
# - TCL -> commit, rollback

# What is Storage Engine
    # Innodb
    # MyISAM

# Reasons that you may have to use certain storage engine
    # amount of data
    # speed and performance
    # functionality
    # max number of rows
    # data integrity

# relational database
# sql is known of declarative programming langugage - non-procedural
# structure Query Language
# - you focused on what and not how part


# Schema

# Data Normalization
    # 1NF
    # 2NF
    # 3NF
    # 4BCNF


# mysql features
    # forieng key support
    # triggers
    # SP
    # FULL TEXT INDEXING AND SEARCHING
    # QUERY CAHCING

# INDEX
    # single column index
    # multi column index (composite index)

# Explain query

# Partition
# Sharding
# Master Slave
# Autoscaling



# what is database
# collection of data stored in a format that can easily be accessed

# Query Execution Order



