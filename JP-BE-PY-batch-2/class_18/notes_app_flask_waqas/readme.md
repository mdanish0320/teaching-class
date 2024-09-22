
# Notes Application Backend APIs

This application provides backend APIs for a simple Notes application, allowing users to create, manage, and organize personal notes and categories. It also includes functionality for user authentication, such as login, signup, and logout.

## Features

- **User Authentication**: Signup, login, and logout.
- **Notes Management**: Create, update, delete, and list personal notes.
- **Categories**: Organize notes into categories.

## Environment Variables

Ensure the following environment variables are set before running the application:

```bash
export MYSQL_USER=your_mysql_username
export MYSQL_PASSWORD=your_mysql_password
```

## How to Run

1. Set up the required environment variables as described above.
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```
4. Import database file `schema_notes_app_waqas.sql`

## Thunder Client Collection

To quickly test the APIs using Thunder Client, you can import the provided collection:

- File: `notes_app_thunder_client_collection.json`

## Dependencies

- Python 3.x
- MySQL
- Flask

Make sure to install all the required dependencies by using the `requirements.txt` file provided with this project.

## Notes

- This application uses MySQL as the database backend. Ensure MySQL is up and running, and the credentials provided in the environment variables are correct.
- Use the provided Thunder Client collection for quick API testing and debugging.
- Database file is also provided `schema_notes_app_waqas.sql`



# notes_app API Documentation
**Client Name**: Thunder Client
**Collection ID**: e33e92bf-afc4-47db-a7fe-80923213161e
**Date Exported**: 2024-09-22T12:56:56.344Z
**Version**: 1.2

## Endpoints

### Auth

#### /signup - create user
- **Method**: POST
- **URL**: http://localhost:3000/api/signup
- **Body**:
```json
{
  "username": "danish",
  "email": "danish@gmail.com",
  "password": "123"
}
```

#### /login
- **Method**: POST
- **URL**: http://localhost:3000/api/login
- **Body**:
```json
{
  "email": "danish@gmail.com",
  "password": "123"
}
```

#### /logout
- **Method**: POST
- **URL**: http://localhost:3000/api/logout

### Categories

#### /categories - create category
- **Method**: POST
- **URL**: http://localhost:3000/api/categories
- **Body**:
```json
{
  "name": "category 1"
}
```

#### /categories - get all categories
- **Method**: GET
- **URL**: http://localhost:3000/api/categories?name=category 1
- **Parameters**:
  - name: category 1

#### /categories/{id} - get one category
- **Method**: GET
- **URL**: http://localhost:3000/api/categories/1