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
# Select few columns from table
# select * from table limit 10
# select * from table order by id ASC or DESC

# column alias
# order by 
# limit
# offset -> for pagination


# WHERE
# single condition
# multip condition
# not condition
# NULL condition
# IN, NOT In Operator
# LIKE
# where
    # And
    # or
    # between
    # is null
    # like
    # date comparison

# JOIN
# inner join
# left join
# right join
# outer join
# cross join
# multiple join
# relationship: one-to-many etc


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

# function
    # distinct
    # https://www.w3schools.com/mysql/mysql_ref_functions.asp


# insert single
# insert multiple
# insert into select from

# update table
# delete from table

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


# exercise: https://github.com/WebDevSimplified/Learn-SQL
# data dump: https://bit.ly/3rvtqdO
# data dump: https://blog.sqlauthority.com/2020/02/15/mysql-download-sample-database-sakila-world-employee/
# data dump: https://github.com/hhorak/mysql-sample-db/blob/master/mysqlsampledatabase.sql
# data dump: https://www.mysqltutorial.org/wp-content/uploads/2018/03/mysqlsampledatabase.zip

# what is database
# collection of data stored in a format that can easily be accessed

# Query Execution Order



