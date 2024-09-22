DROP database if exists waqas_notes_app;
CREATE database if not exists waqas_notes_app;
use waqas_notes_app;

CREATE TABLE users(
   id int auto_increment primary key,
   username varchar(100) not null unique,
   email varchar(255) not null unique,
   password varchar(255) not null,
   created_at datetime DEFAULT CURRENT_TIMESTAMP,
   updated_at datetime DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
   id INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(100) NOT NULL,
   user_id int NOT NULL, 
   created_at datetime DEFAULT CURRENT_TIMESTAMP,
   updated_at datetime DEFAULT CURRENT_TIMESTAMP,

   CONSTRAINT fk_user_category FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);


CREATE TABLE notes (
   id INT AUTO_INCREMENT PRIMARY KEY,
   user_id INT,
   title VARCHAR(255) NOT NULL,
   content TEXT NOT NULL,  -- Use TEXT for larger content
   cat_id INT,
   created_at datetime DEFAULT CURRENT_TIMESTAMP,
   updated_at datetime DEFAULT CURRENT_TIMESTAMP,
   CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE, 
   CONSTRAINT fk_category FOREIGN KEY (cat_id) REFERENCES categories(id)
);

