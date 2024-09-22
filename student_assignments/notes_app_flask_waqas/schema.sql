CREATE database notes;
use notes;

CREATE TABLE users(
   id int auto_increment primary key,
   username varchar(100) not null unique,
   email varchar(255) not null unique,
   createdAt datetime DEFAULT CURRENT_TIMESTAMP,
   password varchar(255) not null 
);

CREATE TABLE categories (
   id INT AUTO_INCREMENT PRIMARY KEY,
   category_name VARCHAR(100) NOT NULL
);


CREATE TABLE notes (
   id INT AUTO_INCREMENT PRIMARY KEY,
   user_id INT,
   title VARCHAR(255) NOT NULL,
   content TEXT NOT NULL,  -- Use TEXT for larger content
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   cat_id INT,
   CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE, 
   CONSTRAINT fk_category FOREIGN KEY (cat_id) REFERENCES categories(id)
);

