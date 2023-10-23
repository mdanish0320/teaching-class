explains nomalization using the following tables

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


