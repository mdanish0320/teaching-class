
# Flask Application with User Authentication and Cookies

## Overview

This is a simple Flask application that demonstrates user authentication (signup, login, and logout) and cookie-based session management. The application allows users to sign up, log in, and access protected APIs if they are logged in. Cookies are used to manage the user session, where a `user_id` cookie is set after a successful login.

### API Endpoints

- **`POST /signup`**: Creates a new user account.
- **`POST /login`**: Logs in a user and sets a cookie with the user ID.
- **`POST /logout`**: Logs out the user and clears the user cookie.
- **`GET /protected-api`**: Returns protected data if the user is logged in.
- **`GET /my-profile`**: Displays the logged-in user's profile.

## API Details

### 1. Signup API

- **Endpoint**: `/signup`
- **Method**: `POST`
- **Description**: Adds a new user to the system.

**Request Example**:

```bash
curl -X POST http://localhost:3000/signup \
-H "Content-Type: application/json" \
-d '{
  "id": "3",
  "email": "user@example.com",
  "password": "user_password"
}'
```

### 2. Login API

- **Endpoint**: `/login`
- **Method**: `POST`
- **Description**: Authenticates a user and sets a `user_id` cookie upon successful login.

**Request Example**:

```bash
curl -X POST http://localhost:3000/login \
-H "Content-Type: application/json" \
-d '{
  "email": "danish@gmail.com",
  "password": "123"
}' \
-c cookies.txt
```

### 3. Logout API

- **Endpoint**: `/logout`
- **Method**: `POST`
- **Description**: Logs out the user by clearing the `user_id` cookie.

**Request Example**:

```bash
curl -X POST http://localhost:3000/logout \
-b cookies.txt -c cookies.txt
```

### 4. Protected API

- **Endpoint**: `/protected-api`
- **Method**: `GET`
- **Description**: Returns protected data if the user is logged in (i.e., has a valid `user_id` cookie).

**Request Example**:

```bash
curl -X GET http://localhost:3000/protected-api \
-b cookies.txt
```

### 5. My Profile API

- **Endpoint**: `/my-profile`
- **Method**: `GET`
- **Description**: Returns the logged-in user's profile.

**Request Example**:

```bash
curl -X GET http://localhost:3000/my-profile \
-b cookies.txt
```

## Understanding Cookies in this Application

### What are Cookies?

Cookies are small pieces of data stored on the client-side (in the user's browser or `curl` session) that allow the server to track and maintain user-specific information across different requests.

In this application, cookies are used to manage user sessions. When a user logs in successfully, the server sets a `user_id` cookie that identifies the logged-in user. This cookie is sent with subsequent requests to verify the user's identity and allow access to protected routes.

### How Cookies are Used

1. **Setting a Cookie on Login**:
   - When a user successfully logs in, a `user_id` cookie is set with the user's ID.
   - This is done using the `set_cookie()` method, which attaches the cookie to the response sent to the client.
   - Example in the `/login` API:
     ```python
     res.set_cookie(
         "user_id",
         str(user['id']),
         path="/",
         # httponly=True
     )
     ```
     The `path="/"` ensures that the cookie is valid for the entire application.

2. **Clearing the Cookie on Logout**:
   - When the user logs out, the `user_id` cookie is cleared by setting its value to an empty string and setting its expiration time to `0`. This effectively deletes the cookie.
   - Example in the `/logout` API:
     ```python
     res.set_cookie("user_id", "", expires=0, path="/")
     ```

3. **Checking the Cookie for Protected Routes**:
   - For protected routes like `/protected-api` and `/my-profile`, the server checks if the `user_id` cookie exists in the incoming request.
   - If the cookie is missing or invalid, the user is asked to log in.
   - Example check in the `/protected-api` and `/my-profile` APIs:
     ```python
     if request.cookies.get('user_id') is None:
         return "please login"
     ```

### Cookie Security

- **HTTP-Only Cookies**: The `httponly=True` option (currently commented out) can be used to mark the cookie as HTTP-only. This means the cookie cannot be accessed via JavaScript, making it more secure by preventing cross-site scripting (XSS) attacks.
  - Uncommenting this in the `/login` API makes the cookie more secure:
    ```python
    res.set_cookie(
        "user_id",
        str(user['id']),
        path="/",
        httponly=True
    )
    ```

- **Expiration and Persistence**: Cookies can be made persistent by setting an expiration time, or they can be session-based (cleared when the browser is closed). The `expires=0` used in the `/logout` API effectively deletes the cookie immediately.

## Conclusion

This application demonstrates the use of cookies for managing user sessions in a Flask application. Cookies provide a simple and effective way to store user session data, enabling login and logout functionality and protecting certain API routes based on whether a user is authenticated.
