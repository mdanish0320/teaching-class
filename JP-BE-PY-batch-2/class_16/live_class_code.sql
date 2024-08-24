use assignment_db;


insert into product (id, name, description, cat_id, created_at) values (1, "item_1", NULL, NULL, NOW());

select * from product;

insert into product (id, name, description, cat_id, created_at) values (1000, "item_2", NULL, 5, NOW());

SET SQL_SAFE_UPDATES = 0;

truncate product;
drop product;
delete from product;


insert into product (name, description, cat_id) values ("item_1", NULL, 100);

select * from product;

insert into product (name, description, cat_id) values ("item_1", NULL, 100);

insert into product (name, description, cat_id) values ("item_1", NULL, 1);

select * from category;
insert into category (name) values("cat_1");

insert into product (name, description, cat_id) values ("item_1", NULL, 1);

delete from product where id = 6;

delete from category where id = 1;
insert into category (name) values("cat_2");

delete from category where id = 2;




update product set cat_id = 100;


https://docs.google.com/spreadsheets/d/1nk__9mvZeo_pmoZW7_nK25BRJoTI4FDOA8hcGjnkBYc/edit?gid=1902750806#gid=1902750806