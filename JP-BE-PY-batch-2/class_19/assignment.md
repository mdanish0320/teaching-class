# Assignment: Update the Notes Application API with Enhanced Session Management

In this assignment, you will enhance the "Building a Notes Application API with Flask" project by implementing a more secure session management system. 

## Objectives:
1. **Update Cookie-Based Session Management**:
   - Replace the current method of storing the `user_id` in the cookie with a more robust approach using a UUID as a `session_id`.
   
2. **Create a User Sessions Table**:
   - Design and implement a new database table called `user_sessions` to store information related to user sessions. This table should include the following fields:
     - `session_id`: UUID (Primary Key)
     - `user_id`: Foreign Key referencing the users table
     - `created_at`: Timestamp indicating when the session was created
     - `expires_at`: Timestamp indicating when the session will expire
     - Additional fields as necessary to support session management (e.g., IP address, user agent).

3. **Enhance Notes Categorization**:
   - Modify the notes feature so that a single note can be assigned to multiple categories. This will involve updating the database schema and ensuring that the API supports this functionality.

## Reference
For details on the original Class 18 assignment, please refer to the following link: [Class 18 Assignment - Building a Notes Application API with Flask](https://github.com/mdanish0320/teaching-class/blob/master/JP-BE-PY-batch-2/class_18/assignment.md#assignment-building-a-notes-application-api-with-flask)
