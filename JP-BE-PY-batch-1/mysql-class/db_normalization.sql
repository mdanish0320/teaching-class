explains nomalization using the following tables

# Relationship exmaples
1. One-to-One Relationship
Example 1: One person can have only one passport.
Example 2: One car can have only one registration number.
Example 3: One employee can have only one company-issued laptop.
2. One-to-Many Relationship
Example 1: One author can write multiple books.
Example 2: One teacher can teach multiple students.
Example 3: One customer can place multiple orders.
3. Many-to-One Relationship
Example 1: Multiple employees can work for one department.
Example 2: Multiple students can enroll in one course.
Example 3: Multiple products can belong to one category.
4. Many-to-Many Relationship
Example 1: Many students can enroll in many courses.
Example 2: Many authors can contribute to many books.
Example 3: Many doctors can treat many patients.  
  
## one to many relation
# one employee can have multiple customers
use classicmodels;
select * from employee;
select * from customer;

# examples
# one country can have multiple citties
# one category can have multiple products
# one company can have multiple employees
# A recipe contains multiple ingrediants
# an order can consists of multiple products
# a customer can order multiple times
# an author can write multiple blogs
# a user can write multiple comments



## many to many relation
# one actor can act in multiple movies
# and one movie can have multiple actors
use sakila;
select * from actor;
select * from film;
select * from film_actor;

# examples
# a teacher can teach multiple subject and the same subject can also be taught by multiple teachers
# a student can enroll in many courses and a single course can be taken by multiple students
# a supplier can have multiple products and a single products can be purchased by multiple suppliers


## one to one relation
A person can have only one National Identity Number
Person and Passport: Each person can have only one passport.


