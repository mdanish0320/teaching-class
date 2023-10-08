# Group By

# get a list of all ratings and find out total rental rate of each rating group
SELECT 
  group_concat(title), 
  rating, 
  SUM(rental_rate), 
  count(*) as total_movies 
FROM 
  film 
  GROUP BY 
rating;
