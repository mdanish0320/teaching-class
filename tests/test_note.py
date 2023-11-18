import pytest
import sys
import random
import string

sys.path.append(".")  # Adds higher directory to python modules path.
from main import app
from db import mysqlconnect, disconnect
from models.users_query import add_new_user
from models.notes_query import add_new_note
from services import token_services

def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

@pytest.fixture()
def add_db_dump():
    # create new db session
    conn = mysqlconnect()
    conn.cursor()
    
    # create new user
    user_id = add_new_user(conn, {
      "name": "danish",
      "email": random_char(5)+"@gmail.com",
      "password": "1234"
    })
    
    # disconnect db session
    disconnect(conn)
    
    # new user ID
    return {
      "user_id": user_id,
      "access_token": token_services.enrypt(user_id)
    }

def test_add_note_api_happy_case(add_db_dump):
  print("new user data", add_db_dump)
  access_token = add_db_dump['access_token']
  
  response = app.test_client().post('/note', json={
    "name": "note 1",
    "description": "test note 1"
  }, query_string={"token": access_token})
  
  data = response.json
  assert type(data['data']) is dict
  assert data['data']['id'] > 0
  
# ADD NOTES TEST CASES
def test_add_note_api_unhappy_case_1_name_field_should_be_required(add_db_dump):
  print("new user data", add_db_dump)
  access_token = add_db_dump['access_token']
  
  response = app.test_client().post('/note', json={
    "description": "test note 1"
  }, query_string={"token": access_token})
  
  data = response.json
  assert data['error']['message'] == "name field is required"
  
def test_add_note_api_unhappy_case_2_description_field_should_be_required(add_db_dump):
  print("new user data", add_db_dump)
  access_token = add_db_dump['access_token']
  
  response = app.test_client().post('/note', json={
    "name": "note 1",
  }, query_string={"token": access_token})
  
  data = response.json
  assert data['error']['message'] == "description field is required"
  
def test_add_note_api_unhappy_case_3_auth_is_required(add_db_dump):
  print("new user data", add_db_dump)
  access_token = add_db_dump['access_token']
  
  response = app.test_client().post('/note', json={
    "name": "note 1",
  })
  
  data = response.json
  assert data['error']['message'] == "Unauthenticated user"


# LIST NOTES TEST CASES
def test_list_notes_happy_case_1_empty_list(add_db_dump):
  print("new user data", add_db_dump)
  access_token = add_db_dump['access_token']
  
  response = app.test_client().get('/note', query_string={'token': access_token})
  
  data = response.json
  assert len(data['data']) == 0
  
  
def _create_note(user_id):
  conn = mysqlconnect()
  conn.cursor()
  note_id = add_new_note(conn, {
      "name": "note 1",
      "description": "test note 1",
      "user_id": user_id
    })
  disconnect(conn)
  return note_id

def test_list_notes_happy_case_2_list_with_1_notes(add_db_dump):
  print("new user data", add_db_dump)
  access_token = add_db_dump['access_token']
  
  # add one note in db for the given user_id
  _create_note(add_db_dump['user_id'])
  
  response = app.test_client().get('/note', query_string={'token': access_token})
  
  data = response.json
  assert len(data['data']) == 1
  
  
def test_list_notes_happy_case_2_list_with_2_notes(add_db_dump):
  print("new user data", add_db_dump)
  access_token = add_db_dump['access_token']
  
  # add two notes in db for the given user_id
  _create_note(add_db_dump['user_id'])
  _create_note(add_db_dump['user_id'])
  
  response = app.test_client().get('/note', query_string={'token': access_token})
  
  data = response.json
  assert len(data['data']) == 2

def test_list_notes_api_unhappy_case_1_auth_is_required(add_db_dump):
  print("new user data", add_db_dump)
  access_token = add_db_dump['access_token']
  
  response = app.test_client().get('/note', json={
    "name": "note 1",
  })
  
  data = response.json
  assert data['error']['message'] == "Unauthenticated user"