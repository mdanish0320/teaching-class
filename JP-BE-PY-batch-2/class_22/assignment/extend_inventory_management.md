Here is an improved and refined version of the new extension requirements:

---

### Extension to Inventory Management System

The Inventory Management System you have developed requires additional functionalities to enhance the overall performance and usability of the application. The new requirements extend the system by adding features related to product tracking, user activity logging, and authentication mechanisms. These enhancements will improve the system's ability to manage supplier relationships, track changes, and enforce security policies.

### New Features to Implement:

1. **Tracking Supplier-Product Quantities**:
   - The current system does not track the quantity of products received from each supplier. Extend the system to manage this information.
   - **Hint**: You can achieve this by taking full control of the **many-to-many** relationship between products and suppliers through an intermediate model (`product_supplier`). This model should contain fields to store:
     - `quantity`: The number of units supplied.
     - `created_at`: The date and time the entry was created.
     - `updated_at`: The date and time the entry was last updated.
   - **Code Hint**: Refer to [Many-to-Many Through Model](https://github.com/mdanish0320/teaching-class/blob/master/JP-BE-PY-batch-2/class_21/many-to-many-through-model.md) for guidance on how to implement a many-to-many relationship through an intermediate table.

2. **User Activity Logging (Product Creation/Deletion)**:
   - The system currently lacks a mechanism to log which users added or deleted products. Implement a solution to track and display this information.
   - **Hint**: Add an authentication mechanism using Django's default User model and track product creation and deletion activities:
     - Implement authentication using **Django's cookie-based authentication**.
     - Create APIs for `login`, `logout`, and `create user`. Only superusers should be allowed to create new users via the API.
     - Use Django's **shell command** to create the initial superuser, ensuring that users created through the API are restricted from accessing the Django admin interface.
   - **Note**: This will require updating the product model to store a reference to the user who created or deleted a product.

3. **Enhanced Dashboard Metrics**:
   - Extend the dashboard to include additional statistics and metrics for products and suppliers.
   
   **Product Metrics**:
   - Display the total number of products.
   - For each category, show the number of products under that category.
   - For each supplier, display the number of products supplied by that supplier.

   **Supplier Metrics**:
   - For each supplier, display the total value of products supplied (calculated as `price * stock quantity`).
   - Summarize suppliers based on the **highest and lowest number of supplied products**.

4. **Authentication and Authorization**:
   - Ensure that only authenticated users can add, update, or delete products, suppliers, and categories. Guest users should only be able to view the data via `GET` APIs.
   - **Hint**: Use Django's permission system to enforce these rules:
     - Reference this [Permissions Class](https://github.com/mdanish0320/teaching-class/blob/master/JP-BE-PY-batch-2/class_22/user-permissions/api/permissions.py) and [Permissions Classification](https://github.com/mdanish0320/teaching-class/blob/master/JP-BE-PY-batch-2/class_22/permissions-classification.md) for guidance on implementing user permissions.
     - Implement role-based permissions ensuring only superusers can perform specific actions like user creation.

---

### Additional Requirement:

After completing the above tasks using **cookie-based authentication**, create a separate project. Copy the entire codebase and modify the authentication mechanism to use **JWT-based authentication** instead of cookie sessions.
