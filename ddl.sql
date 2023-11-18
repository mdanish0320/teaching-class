CREATE DATABASE IF NOT EXISTS google_notes;
USE google_notes;

DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS category;
CREATE TABLE category (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS note;
CREATE TABLE note (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    description TEXT NOT NULL,
    user_id INT UNSIGNED NOT NULL,
	PRIMARY KEY (id),
    KEY fk_user_id_idx (user_id),
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES user(id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

DROP TABLE IF EXISTS note_category;
CREATE TABLE note_category (
    note_id INT UNSIGNED NOT NULL,
    category_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (note_id, category_id),
    CONSTRAINT fk_note_id FOREIGN KEY (note_id) REFERENCES note (id),
    CONSTRAINT fk_category_id FOREIGN KEY (category_id) REFERENCES category (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

