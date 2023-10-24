# use flask documentation https://flask.palletsprojects.com/en/3.0.x
# install flask
# run server
# explain server port (again)
# create APIs without class view or blueprint
  # test APIs
  # /home and /profile and /add_employee and /get_employee
# HTTP Methods and use postman to invoke api
  # GET query string and path_parameters
  # POST form-data and form-url-encoded and raw
  # class-assignment: in-memory CRUD using get, post PUT and Patch and Delete
  # class assignment: create 3 API login (POST API), signup (POST API) and /my_profile with db
    # data validation

# assignment
  # persistent storage CRUD on file and db using proper get/post/put/delete methods
# explain HTTP Methods
  # invoke api via command line
  # invoke api via postman
  # invoke api via python request module


# login/signup with session
  # session cookie and jwt
# authentication methods

# Hashing Passwords With Werkzeug
# pagination
# logging
# error handling: http errors
# pytest
# signal
# https://flask.palletsprojects.com/en/3.0.x/patterns/streaming/
# https://flask.palletsprojects.com/en/3.0.x/security/
# async await

# sql-alchemy
# production ready server - wsgi/gunicor 
# deployment

# project file-structure: small project management
# create apis with view as function
# create apis with class view

# project file-structure: big project magagement
# create apis with blueprint with view fuction
  # # Blueprint
  # give you a feature to group endpoints and then you can add that group in the flask app
# create apis with blueprint with class view

# Data Validation + Swagger API Documention
# flask-smorest Requires: Python >=3.8

## Concept
# OSI Model
# TCP Connection and its possible values
# TCP -> HTTP, Text, Email, video streaming services
# UTCP -> VoIP, Live video Streaming, DNS, Online Games
# HTTP Requests/Response - https://www.youtube.com/watch?v=76CcJ90Lz4U
# General headers
# Http Request Method: get, post, put, delete
  # POST: https://www.atatus.com/blog/http-post-request-method/
  # Authorization: https://compile7.org/decompile/authorization-request-headers-explained/
  # status code
  # image: https://www.seobility.net/en/wiki/images/d/d2/HTTP-Header.png
  # image: https://mkyong.com/wp-content/uploads/2016/01/view-header-in-chrome.png
# HTTP Reponse Header:
  # Access-Control-Allow-Origin
  # Content-Type
# Diff between POST and PUT: POST supposed to create new record in db and PUT doesn’t. Calling PUT API multiple times should not create any new record in db but calling POST API multiple times tends to create new record in db.
# Content types 
# Web services 
  # Rest vs soap
  # Rest vs restful - https://www.youtube.com/watch?v=UJgq1tEwMBk




# differnet extensions fo Flask API
flask-restplus is a fork of flask-restful
restplus is unmainted and a new forked repo is named as Flask-RESTX 
flask-smorest (formerly known as flask-rest-api) 

flask-smorest vs Flask-RESTX 

Flask-RESTX requires Python 3.7+.
flask-smorest Requires: Python >=3.8

