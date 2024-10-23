### Assignment: Database Design for Blogging Application

#### Instructions:
You are tasked with creating a **database design** for a blogging application. This will involve defining the structure of the database, creating tables, and establishing relationships between these tables. Use **MySQL Workbench** to create the database, tables, and relationships, then export the database as an `.sql` file and generate an **Entity-Relationship Diagram (ERD)** for review.

### Requirements:

The blogging application needs to support multiple users with different roles (e.g., authors, superusers, moderators), posts, categories for organizing content, comments, and the ability to like both posts and comments. One key feature is that each post can have **one owner** and **multiple co-authors**.

Use these requirements as hints to guide your design.

---

### Key Features (Hints):

- The application will have different types of users such as:
    - **Superuser**: Has full control over the platform, can manage all content and users.
    - **Moderator**: Can moderate content such as posts and comments.
    - **Author**: Can create, update, and manage their own posts.
    - **Reader**: Can only view the blogs, like the blog/comment and provide comment.
  - The blog will consist of posts written by users (specifically authors).
  - Each post will have one **owner** (the main author) but can also have **co-authors** who contribute to the post.
  - Each post can belong to one or more **categories** for better organization.
  - Logged in Users can comment on posts.
  - Logged in Users should be able to like both **posts** and **comments**.
