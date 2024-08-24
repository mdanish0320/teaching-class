explanation
https://docs.google.com/spreadsheets/d/1nk__9mvZeo_pmoZW7_nK25BRJoTI4FDOA8hcGjnkBYc/edit?gid=1358049455#gid=1358049455

table: user contains 10 millions rows
id	fname	lname	email	country	created_at	updated_at

what time it will take to fetch the data with the command
select * from users;
# assume 10 seconds


# what time it will take to fetch the data with country "pakistan" (suppose it has 1 million rows of pakistan)
select * from users where country = "pakistan"'; 

# how a human search in dictionary
# indexing works similar way

# the below command will still take long to fetch this single user
# even though we know the email is unique (but unique constraint is not used)
select * from users where email= "marij@gmail.com"'; 
select * from users where email= "abdullah@gmail.com"

# in case abdullah is the first row in the table (without indexing)
# interupting the mysql loop to find more data
select * from users where email= "abdullah@gmail.com" limit 1


explain indexing column order
"""
select * from users where fname = "" and lname = ""
select * from users where lname = "" and fname = ""

select * from users where fname = "" 
select * from users where lname = "" 


(fname, lname)
(fname, lname, country)
select * from users where fname = "" and lname = "" and country=""
select * from users where fname = "" and lname = ""
select * from users where lname = "" and country=""


select * from users where fname = "" and lname = "" and country=""
"""

# if indexing is so good, why are we not use it in all columns of the TABLE
# its because of the indexing data structure that favours data fetching but oppose data insert/update/DELETE
# indexing data structure is B+Tree (self balancing tree)
# left side of the tree will always have the lower values and right side will have higher VALUES
# leaf node will always contains the whole data
# Clustered vs NON clustered INDEX
# leaf of the clustered index will contain actual data
# leaf of the non-clustered index wil contains ref of the actual data

# B+Tree demonstration
https://www.cs.usfca.edu/~galles/visualization/BPlusTree.html

# BTree demonstration
https://www.cs.usfca.edu/~galles/visualization/BTree.html

# the algorithm to search the data in B+Tree is Binary Search
