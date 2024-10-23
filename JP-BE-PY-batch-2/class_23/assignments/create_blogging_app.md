### Assignment: Blogging Application Development

#### Instructions:
You are tasked with creating a **blogging application** that will allow users to create, manage, and interact with blog posts. The application will support different user roles, including superusers and authors, and will have features such as categorizing posts, commenting, and liking both posts and comments. You will need to implement APIs to handle these functionalities and ensure that the application meets the defined requirements.

You must also implement features that allow authors and superusers to see various statistics related to posts, comments, and likes.

### Requirements:

The blogging application must meet the following functional and non-functional requirements:

---

### Key Features:

- **User Roles**:
  - **Superuser**:
    - Can manage all content and users.
    - Can view the total number of posts, the total number of comments, and the total number of likes across the entire platform.
  - **Author**:
    - Can create, update, and delete their own posts.
    - Can view the total number of posts they've created.
    - Can view the total number of comments and likes for each of their posts.
    - Can add co-authors to their posts.
  - **Moderator**:
    - Can moderate content such as posts and comments.
  - **Reader**:
    - Can view blog posts, like posts and comments, and leave comments.

---

### Application Features:

1. **Authentication and Authorization**:
   - Implement user registration and login.
   - Ensure role-based access control (RBAC) so that different users have access to only their permitted features.

2. **Blog Posts**:
   - Authors can create and manage their own blog posts.
   - Each post should have one **owner** (main author) but can also have **co-authors**.
   - Posts can belong to one or more **categories**.
   - Posts should display the total number of **comments** and **likes**.
   - Superusers can view all posts across the platform.

3. **Categories**:
   - Posts can be organized by categories.
   - Users should be able to view posts by category.

4. **Comments**:
   - Logged-in users can comment on posts.
   - Users can like comments.

5. **Likes**:
   - Logged-in users can like posts and comments.
   - Each post and comment should display the number of likes it has received.

---

### Author Statistics:

- Authors should be able to view:
  - The total number of posts they have created.
  - The total number of comments on each of their posts.
  - The total number of likes on each of their posts.

### Superuser Statistics:

- Superusers should be able to view:
  - The total number of posts created on the platform.
  - The total number of comments on all posts.
  - The total number of likes across all posts and comments.
