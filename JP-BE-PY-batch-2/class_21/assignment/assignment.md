### Inventory Management System Requirements

The Inventory Management System is designed to manage products, categories, and suppliers efficiently. The system should allow users to perform CRUD (Create, Read, Update, Delete) operations for products, categories, and suppliers. Additionally, it will handle relationships between these entities, specifically a **one-to-many** relationship between products and categories, and a **many-to-many** relationship between products and suppliers.

### Application Functionality:

1. **Product Management**:
   - The system should allow users to create, update, delete, and view details of products.
   - Each product can belong to one category.
   - Each product can have multiple suppliers, and each supplier can supply multiple products.
   - The product list should display:
     - Product details (e.g., id, name, description, price quantity, created_at, updated_at)
     - The category to which the product belongs (i.e id, name).
     - The names of all suppliers associated with the product (id, name).
   - When updating a product, the user should be able to modify its associated category and suppliers.
   - When adding the product category and supplier should be optional

2. **Category Management**:
   - The system should allow users to create, update, delete, and view categories.
   - Each category can have multiple products.
   - When a category is deleted, products associated with it should either be reassigned to NULL, deleted through a cascade operation, or restricted from deletion, depending on the desired business rule.
   - The category list should display:
     - Category details (e.g., name, description)
     - The number of products associated with each category.

3. **Supplier Management**:
   - The system should allow users to create, update, delete, and view suppliers.
   - Each supplier can supply multiple products.
   - The supplier list should display:
     - Supplier details (e.g., name, contact information)
   - ~~When updating a supplier, the user should be able to manage the products associated with that supplier.~~

4. **Product Listing**:
   - The product list view should include:
     - Product name, description, price, and stock quantity.
     - The name of the category the product belongs to.
     - A list of all suppliers providing the product.
   - The list should be filterable by category and supplier.
   - Users should be able to search for products by name, category_id and supplier_id

5. **Category-Product Relationship**:
   - Each product should be linked to a single category (one-to-many relationship between products and categories).
   - Users should be able to assign or change the category of a product when adding or updating the product.

6. **Supplier-Product Relationship**:
   - Products should be able to have multiple suppliers, and suppliers should be able to provide multiple products (many-to-many relationship between products and suppliers).
   - Users should be able to assign multiple suppliers to a product when adding or updating the product.
   - Users should be able to assign multiple products to a supplier when adding or updating the supplier.

### NOTE:
You could use the provided CSV data, if you want.


### Additional Metrics and Statistics Requirements:

1. **Product Metrics**:
   - The system should display the total number of products.
   - For each category:
     - Display the number of products under that category.
   ~~- For each supplier:~~
     ~~- Display the number of products supplied by each supplier.~~
   - Provide a report on the **total stock quantity** per product category.
   - Show the **average price** of products within each category.

2. **Category Metrics**:
   - For each category:
     - Display the total number of products belonging to that category.
     - Display the total stock quantity of products in that category.
   
3. **Supplier Metrics**:
   - For each supplier:
     - Display the number of products they provide.
     ~~- Show the total value of products supplied by each supplier (price * stock quantity).~~
     - Provide a summary of suppliers with the **highest and lowest number of supplied products**.
   - For each supplier:
     - Show a list of products they supply, grouped by category.

