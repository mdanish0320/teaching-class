# In-Memory CRUD Application with Flask

This project demonstrates a simple CRUD (Create, Read, Update, Delete) API for managing a collection of books. The application uses Flask to handle HTTP requests and provides the following functionalities:

### API Endpoints

- **POST** `/books`: Add a new book to the collection.
- **GET** `/books`: Retrieve all books from the collection.
- **GET** `/books/{id}`: Get a single book by its ID.
- **PUT** `/books/{id}`: Update the name of an existing book by its ID.
- **DELETE** `/books/{id}`: Delete a book from the collection by its ID.

> **Hint**: You can refer to this [video tutorial](https://www.youtube.com/watch?v=n4orudncbTs) for guidance.

---

# Class 15 Assignment Enhancement

In this project, you will expand the previous Class 15 assignment by integrating Flask to create API endpoints that handle CRUD operations for categories and products in an e-commerce application. You will be using the [provided database file](https://github.com/mdanish0320/teaching-class/blob/master/JP-BE-PY-batch-2/class_17/db.sql) to manage categories and products data. Your task is to create API routes that allow adding, updating, deleting, and retrieving information from the database.

## Requirements

### 1. Categories API
- **Create API to add categories**:  
    - Add the following 3 categories to the system:
        - Electronics  
        - Furniture  
        - Books  
    - You will create a POST API that allows adding new categories to the database.

### 2. Products API
- **Create API to add products**:  
    - Add the following 5 products under the appropriate categories:
        - Laptop (Electronics)  
        - Smartphone (Electronics)  
        - Table (Furniture)  
        - Chair (Furniture)  
        - Kids Bed Time Story (Books)  
    - Your API should allow specifying the category ID when adding a product, ensuring that products are correctly assigned to their categories.

### 3. Update Products API
- **Create API to update products**:  
    - Update the names of the following products:
        - Rename "Laptop" to "Gaming Laptop"  
        - Rename "Chair" to "Computer Chair"  
    - Create a PUT API that allows updating a product’s name based on its ID.

### 4. Delete Products API
- **Create API to delete products**:  
    - Remove the product "Kids Bed Time Story" from the product list.
    - This will be a DELETE API where you can delete a product by its ID.

### 5. Display Categories API
- **Create API to retrieve all categories**:  
    - This API should return a list of all available categories in the system.
    - Use a GET request to display the data.

### 6. Display Products API
- **Create API to retrieve all products**:  
    - This API should return a list of all products, including their category associations.
    - Use a GET request to retrieve the data.

### 7. Display Combined Products and Categories API
- **Create API to display both products and categories combined**:  
    - This API should display all products along with their associated categories in a structured format.
    - Use a GET request to display the data.

### 8. Display Product Count API
- **Create API to display the count of products**:  
    - This API should return the total number of products currently available in the system.
    - Use a GET request to display the product count.
