# creating last assignment database design
# it contains 2 table: product and category
# https://github.com/mdanish0320/teaching-class/blob/master/JP-BE-PY-batch-2/class_15/python_mysql_connection_assignment_db/db.sql

# create database "assignment_db" using mysql workbench
# explain characterset and collation
# create category table with constraint
# create table product without any CONSTRAINT


# start QUERY
use assignment_db;

# because we didn't add any CONSTRAINT in product table
# following data is allowed to add
insert into product (id, name, description, cat_id, created_at) values (1, NULL, NULL, NULL, NOW());
Anomalies:
id is added manualy
product name IS NULL
cat_id IS NULL
created_at is added manaully


insert into product (id, name, description, cat_id, created_at) values (2, "item_1", NULL, NULL, NOW());
Anomalies:
id is added manualy
cat_id IS NULL
created_at is added manaully


select * from product;


insert into product (id, name, description, cat_id, created_at) values (1000, "item_2", NULL, 5, NOW());
Anomalies:
id is added manualy and value is not incremented
cat_id IS added to be "5" but category table doesn't have data
created_at is added manaully


# remove all data from table product
SET SQL_SAFE_UPDATES = 0;

# trunacte delete the whole data and also reset the AUTOINCREMENT counter
truncate product;

# "delete" command only deletes whole data but doesn't reset AUTOINCREMENT counter;
delete from product;

# to remove anomalies of
id needs to be added manualy
product name IS NULL allowed
cat_id IS NULL allowed
created_at is added manaully

# we need to add constraint in product TABLE
- id AUTOINCREMENT and PRIMARY KEY
- product name NOT NULL
- created_at default NOW()
- cat_id FOREIGN KEY RESTRICT


# product without name is not allowed
# product without cat_id is not allowed either
# cat_id must exists in category table
insert into product (name, description, cat_id) values ("item_1", NULL, 1);

# explain deletion and updation of parent and child table when FOREIGN KEY RESTRICT is used
select * from category;
insert into category (name) values("cat_1");

insert into product (name, description, cat_id) values ("item_1", NULL, 1);

delete from product where id = 6;

delete from category where id = 1;
insert into category (name) values("cat_2");

delete from category where id = 2;




update product set cat_id = 100;