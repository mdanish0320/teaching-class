SET SQL_SAFE_UPDATES = 0;
UPDATE category SET COL_NAME = VALUE WHERE COL_NAME = VALUE_2;
UPDATE category SET last_update = "2023-01-01" where name = 'Action' ;
UPDATE category SET last_update = "2023-01-01", name = "Action" where name = 'Action_2' ;
