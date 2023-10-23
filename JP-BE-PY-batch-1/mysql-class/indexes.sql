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

explain select * from users where name = "danish" and emal =  '2023-12-21';

CREATE INDEX idx_name
ON users (`name`);

explain select * from users where name = "danish" and emal =  '2023-12-21';
