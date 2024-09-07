# Basic Structure

- **Base URL**: `http://localhost:3000` (Represents the root of the API).
- **Resources**: Represents the entities or collections within the API.
- **Sub-resources**: Represents resources related to a parent resource.

## Examples

### Single Resource:
- **URL**: `/users`
  - **Description**: Represents a collection of user resources.

- **URL**: `/users/{userId}`
  - **Description**: Represents a specific user resource identified by `userId`.

### Nested Resources:
- **URL**: `/users/{userId}/posts`
  - **Description**: Represents a collection of posts belonging to a specific user.

- **URL**: `/users/{userId}/posts/{postId}`
  - **Description**: Represents a specific post belonging to a specific user.

### Further Nesting:
- **URL**: `/users/{userId}/posts/{postId}/comments`
  - **Description**: Represents a collection of comments for a specific post of a specific user.

- **URL**: `/users/{userId}/posts/{postId}/comments/{commentId}`
  - **Description**: Represents a specific comment on a specific post of a specific user.

---

# Products

- **URL**: `/products`
  - **Description**: Represents the collection of products.

- **URL**: `/products/{productId}`
  - **Description**: Represents a specific product.

# Categories

- **URL**: `/categories`
  - **Description**: Represents the collection of categories.

- **URL**: `/categories/{categoryId}/products`
  - **Description**: Represents products within a specific category.

# Orders

- **URL**: `/orders`
  - **Description**: Represents the collection of orders.

- **URL**: `/orders/{orderId}/items`
  - **Description**: Represents items within a specific order.
