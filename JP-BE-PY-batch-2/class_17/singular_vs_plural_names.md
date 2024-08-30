# Plural vs. Singular Resource Names

## Recommended Practice

### Use Plural Names for Collections
This is the most common and widely accepted convention for RESTful API design. Plural names are used to represent collections of resources.
- **Example:** `/users` (for a collection of users)
- **Example:** `/orders` (for a collection of orders)

### Use Singular Names for Individual Resources
When referring to a single instance of a resource, use the singular form. This approach maintains consistency with the plural names used for collections.
- **Example:** `/users/{userId}` (for a specific user)
- **Example:** `/orders/{orderId}` (for a specific order)

## Summary
Using plural names for collections and singular names for individual resources is a standard practice in RESTful API design. This approach maintains consistency and makes the API intuitive for developers familiar with RESTful conventions.

## Plural Mysql Table Names
It’s common to use plural names for tables in databases because they represent collections of entities.
- **Example:** `users` for the collection of user records
- **Example:** `employees` for the collection of employee records

## MySQL Table and Model Names - Singular or Plural

### Singular Model Names
Define your SQLAlchemy model classes with singular names. This convention represents a single entity and aligns with the concept of the model being a representation of one record.
- **Example:** For a table named `users`, define the model class as `User`.
- **Example:** For a table named `employees`, define the model class as `Employee`.
