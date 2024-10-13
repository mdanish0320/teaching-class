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
   

---

### Task Breakdown:
1. **Create the Database**: Use MySQL Workbench to create a new database for the blogging application.

2. **Define the Tables**:
   - Define tables for each of the features described above (e.g., users, posts, categories, comments, likes, etc.).
   - Ensure that the relationships between the tables are established correctly (e.g., one-to-many and many-to-many).

3. **Establish Relationships**:
   - Set **primary keys** and **foreign keys** as needed to ensure data integrity.
   - Ensure that each post is associated with a user (author), each comment is linked to a post and a user, and categories can be linked to multiple posts.

4. **Generate the ERD**:
   - Once you have completed the database design, use MySQL Workbench to generate an **ERD (Entity-Relationship Diagram)** to visually represent the database structure.
   - hint: (class_16 revision_tutorials.txt)[https://github.com/mdanish0320/teaching-class/blob/master/JP-BE-PY-batch-2/class_16/revision_tutorial.txt#L30C1-L31C44]

5. **Export the Database**:
   - Export the database design as a `.sql` file (the export should include the schema for all tables and relationships).
   - hint: (class_16 revision_tutorials.txt)[https://github.com/mdanish0320/teaching-class/blob/master/JP-BE-PY-batch-2/class_16/revision_tutorial.txt#L27C1-L28C44]

---

### Submission:
- Submit the **ERD** for review.
- Provide the **exported database schema** as a `.sql` file.

Good luck!