# functions

# Unique values
Select DISTINCT rating from film;

# COUNT
SELECT COUNT(*) AS total_emp FROM employees

# SUM
SELECT SUM(buyPrice) FROM products

# AVG
SELECT AVG(buyPrice) FROM products

# MAX
SELECT MAX(buyPrice) FROM products

# MIN
SELECT MIN(buyPrice) FROM products

# LOWER
SELECT lower(productName) FROM products


# DATE -> MONTH
SELECT * FROM orders WHERE MONTH(orderDate) = 1

# DATE -> MONTH + YEAR
SELECT * FROM orders WHERE YEAR(orderDate) = 2003 OR MONTH(orderDate) = 1

# DATE -> DAY + MONTH + YEAR
SELECT
    *
FROM
    orders
WHERE
    YEAR(orderDate) = 2003
    AND MONTH(orderDate) = 1
    AND DAY(orderDate) = 6

# DATE
SELECT
    *
FROM
    orders
WHERE
    DATE(orderDate) = "2003-01-06"

# WHEN TO USE DATE FUNCTION?
SELECT
    *
FROM
    orders
WHERE
    orderDate = "2003-01-06"

# example 1
SELECT
    *
FROM
    rental
WHERE
    rental_date = "2005-05-24 22:53:30"

# example 2
SELECT
    *
FROM
    rental
WHERE
    DATE(rental_date) = "2005-05-24"

# hacky solution
SELECT
    *
FROM
    rental
WHERE
    rental_date LIKE "2005-05-24%"


# HOW does date function works when applying to the column that contains datetime
SELECT DATE(rental_date) FROM rental

# class task: get 25 days older data from the date 2005-05-25
# 2005-05-25
# 25 days

# solution 1
SELECT
    *
FROM
    payment
WHERE
    DATE(payment_date) BETWEEN "2005-05-25" AND "2005-06-19"

# proper solution
# DATE_ADD
SELECT
    *
FROM
    payment
WHERE
    DATE(payment_date) BETWEEN "2005-05-25" AND date_add(
        "2005-05-25",
        Interval 25 Day
    )

# how does the interval function works
select date_add(
    "2005-05-25",
    Interval 25 Day
) as dt



# class work: inverse condition
# DATE_SUB
SELECT
    *
FROM
    payment
WHERE
DATE(payment_date) BETWEEN
date_sub(
    "2005-06-19",
    Interval 25 Day
    )
AND
"2005-06-19"


# Display Current Date with time
select NOW()

# Display Current Date only
select DATE(NOW())


# class work: get 15 days older date from current time
SELECT * FROM payment
where payment_date BETWEEN DATE_SUB(NOW(), INTERVAL 15 DAY) AND NOW()