# insert
select * from offices;

# insert syntax 1
INSERT INTO TABLE_NAME () VALUES ();
INSERT INTO offices (
officeCode, city, phone, addressLine1, addressLine2,
state, country, postalCode, territory
) VALUES (1001, 'karachi', '123', 'xyz', 'abc', 'sindh', 'pakistan', '123', 'garden');

# insert syntax 2
INSERT INTO TABLE_NAME VALUES ();
INSERT INTO offices VALUES (1002, 'hyderabad', '123', 'xyz', 'abc', 'sindh', 'pakistan', '123', 'garden');

# insert syntax 3
INSERT INTO TABLE_NAME VALUES (), (), (), ();
INSERT INTO offices VALUES 
  (1003, 'peshawar', '123', 'xyz', 'abc', 'sindh', 'pakistan', '123', 'garden'),
  (1004, 'larkana', '123', 'xyz', 'abc', 'sindh', 'pakistan', '123', 'garden'),
  (1005, 'murree', '123', 'xyz', 'abc', 'sindh', 'pakistan', '123', 'garden');


# update syntax
SET SQL_SAFE_UPDATES = 0;
UPDATE offices SET city = "hyderabad" WHERE city = "karachi";

# DELETE syntax
DELETE FROM TABLE WHERE COL_NAME = VALUE;