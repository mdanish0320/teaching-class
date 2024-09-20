# E-Commerce Database and Flask API Assignment
In this project, you will expand the previous Class 16 assignment by integrating Flask to create API endpoints that handle CRUD operations.
Please create centralized routers using `app.add_url_rule()`. Use your own database and data that you created on assignment 16.

## API List

Below is the list of APIs that you need to create for this assignment. All APIs should follow RESTful principles and ensure secure data handling.

### 1. **Category APIs**
- **POST** `/api/categories` - Add a new category.
- **GET** `/api/categories` - Retrieve a list of all categories.

### 2. **Product APIs**
- **POST** `/api/products` - Add a new product.
- **GET** `/api/products` - Retrieve a list of products with category details (supports filtering via query parameters).
  - Query Parameters:
    - `category` (string) - Filter by category name.

### 3. **Customer APIs**
- **POST** `/api/customers` - Add a new customer.
- **GET** `/api/customers` - Retrieve a list of customers.

### 4. **Order APIs**
- **POST** `/api/orders` - Add a new order.
- **GET** `/api/orders` - Retrieve a list of orders with customer and product details (supports filtering via query parameters).
  - Query Parameters:
    - `customer_name` (string) - Filter by customer name.
    - `order_date` (date) - Filter by order date.
    - `product_name` (string) - Filter by product name.

### 6. **Payment APIs**
- **POST** `/api/payments` - Add a new payment.


### 7. **Metrics APIs**
- **GET** `/api/metrics/sales` - Retrieve sales metrics.
  - Query Parameters:
    - `start_date` (date) - Start date for sales metrics.
    - `end_date` (date) - End date for sales metrics.
- **GET** `/api/metrics/orders` - Retrieve order metrics.
  - Query Parameters:
    - `start_date` (date) - Start date for order metrics.
    - `end_date` (date) - End date for order metrics.
- **GET** `/api/metrics/payments` - Retrieve payment metrics.
  - Query Parameters:
    - `start_date` (date) - Start date for payment metrics.
    - `end_date` (date) - End date for payment metrics.
- **GET** `/api/metrics/products` - Retrieve product metrics (inventory levels, out of stock).
- **GET** `/api/metrics/geography` - Retrieve geographical sales metrics.

## Notes:
- Use appropriate HTTP status codes for success and error responses (e.g., `200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`).
- Ensure that data input is validated and protected from SQL injection or other vulnerabilities by using parameterized queries or ORM.



__________________________________________________________________________________________________________________________________________


## Assignment: Building a Notes Application API with Flask

### Overview

In this assignment, you will create a simple Notes Application API using Flask and Mysql. The application will allow users to sign up, log in, and perform basic operations such as creating, updating, and deleting notes. Each note can be categorized, and users can only view and manage their own notes. Authentication will be managed via cookies.

Create mysql database design that suits the below application requirements.

### Features to Implement

1. **Signup**
   * Implement an API for user registration.
   * Each user should have a unique username and password.
   * Passwords must be stored securely (use hashing algorithms such as bcrypt).
   * Endpoint:
     * POST /signup
   * Request Body:
     ```json
     {
        "username": "string",
        "password": "string"
     }
     ```

2. **Login**
   * Implement an API for user login.
   * After successful login, set an authentication cookie for the user.
   * Return a proper status message if login fails.
   * Endpoint:
     * POST /login
   * Request Body:
     ```json
     {
        "username": "string",
        "password": "string"
     }
     ```
   * Response: Set a session cookie to authenticate the user for future requests.

3. **Create Notes**
   * Users should be able to create new notes.
   * Each note should contain a title, content, and optionally be assigned to a category.
   * Endpoint:
     * POST /notes
   * Request Body:
     ```json
     {
        "title": "string",
        "content": "string",
        "category_id": "integer"  // Optional
     }
     ```
   * Note: Ensure that only authenticated users can create notes.

4. **Update Notes**
   * Allow users to update the title, content, or category of their own notes.
   * Endpoint:
     * PUT /notes/{note_id}
   * Request Body:
     ```json
     {
        "title": "string",
        "content": "string",
        "category_id": "integer"  // Optional
     }
     ```

5. **Delete Notes**
   * Allow users to delete their own notes.
   * Endpoint:
     * DELETE /notes/{note_id}
   * Note: Only allow authenticated users to delete their own notes.

6. **Create Category**
   * Implement an API to create categories for organizing notes.
   * Each category should have a unique name.
   * Endpoint:
     * POST /categories
   * Request Body:
     ```json
     {
        "name": "string"
     }
     ```

7. **Assign Category to a Note**
   * Notes can be assigned to a category during creation or update.
   * Ensure that only existing categories can be assigned.
   * Endpoint:
     * PUT /notes/{note_id}
   * Request Body:
     ```json
     {
        "category_id": "integer"
     }
     ```

8. **List Notes with Filtering**
   * Implement an API that lists all notes for the authenticated user.
   * Allow users to filter their notes based on:
     * Title
     * Category
     * Date Created
   * Endpoint:
     * GET /notes
   * Query Parameters (Optional):
     * title, category_id, date_created
   * Example request:
     ```bash
     GET /notes?title=shopping&category_id=1
     ```

9. **View Only User's Own Data**
   * Ensure that users can only view, update, or delete their own notes.
   * Implement proper authorization checks in each API.
   * Endpoint:
     * GET /notes/{note_id}
   * Note: Return an error if a user tries to access another user's note.

10. **Authentication via Cookies**
   * Use cookies for managing user authentication.
   * Store the session information in the cookies, and validate cookies in each request.
   * Ensure that protected routes (like creating, updating, and deleting notes) require a valid authentication cookie.
