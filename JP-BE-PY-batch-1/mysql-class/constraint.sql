# constraint
USE hr_db;
select * from employees order by employee_id dESC;

# duplicate entry on primary key
insert into employees values ('100', 'Steven', 'King', 'SKING', '515.123.4567', '1987-06-17', 'AD_PRES', '24000.00', '0.00', '0', '90'
);

# duplicate entry on email
insert into employees values ('100', 'Steven', 'King', 'SKING', '515.123.4567', '1987-06-17', 'AD_PRES', '24000.00', '0.00', '0', '90'
);

# NOT NULL
insert into employees values ('1001', 'Steven', NULL, 'SKING_gmai.com', '515.123.4567', '1987-06-17', 'AD_PRES', '24000.00', '0.00', '0', '90'
);


# Foreign Key example
USE classicmodels;
select * from customers;
insert into customers values(
  '100001', 'Atelier graphique', 'Schmitt', 'Carine ', '40.32.2555', '54, rue Royale', NULL, 'Nantes', NULL, '44000', 'France', '13700000', '21000.00'
)  