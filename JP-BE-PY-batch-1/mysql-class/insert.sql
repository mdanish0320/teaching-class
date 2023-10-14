SELECT * FROM sakila.category;

INSERT INTO category VALUE(17, "EXAMPLE_1", "2023-01-01");

# strict column order
INSERT INTO category VALUE("EXAMPLE_1", 17,  "2023-01-01");

# specify column order
INSERT INTO category (name, category_id, last_update) VALUES ("example_2", 20, "2023-02-02");

# mutli insert
INSERT
INTO
category (name, category_id, last_update)
    VALUES ("example_5", 23, "2023-02-02"), ("example_6", 25, "2023-02-02"), ("example_7", 27, "2023-02-02");
