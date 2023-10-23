CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

select * from Persons;


CREATE TABLE users (
    id int,
    name varchar(255),
    email varchar(255),
    dob varchar(255),
    is_married varchar(255),
    address varchar(255),
    status varchar(255),
    salary varchar(255)
);
select * from users;
DROP TABLE users;



CREATE TABLE `sakila`.`users` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `emal` VARCHAR(100) NOT NULL,
  `is_married` TINYINT NOT NULL,
  `dob` DATE NOT NULL,
  `address` TEXT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `a` (`emal` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;