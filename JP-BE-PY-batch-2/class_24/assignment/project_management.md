Here is a more structured version of the assignment with proper headings, instructions, and details for each feature:

---

## **Assignment: Basic Project Management Application (Similar to JIRA)**

### **Objective:**
Students will build a basic project management application that includes user roles, project management, and task management features. The application will simulate core functionality similar to JIRA, providing role-based access to different parts of the system.

### **Instructions:**
- You are required to implement both the backend and frontend of the application.
- The application should include authentication, user roles, project management, and task management functionalities.
- Ensure proper validation, error handling, and secure code practices.

---

### **1. User Roles & Authentication**

#### **User Roles:**
Your application should support the following roles:
1. **Admin**: Full access to the system, including user management and project creation.
2. **Project Manager**: Can create and manage projects, assign tasks to users.
3. **Developer**: Can manage tasks assigned to them.
4. **Tester**: Can manage tasks assigned to them.

#### **Authentication & Authorization:**
- **Sign up, Log in, Log out**: Users should be able to register, log in, and log out of the application.
- **Role-based Access Control**:
  - **Admin**: Admins should have access to manage users, create projects, and assign roles to users.
  - **Project Manager**: Project Managers can create projects and assign tasks to Developers and Testers.
  - **Developers & Testers**: These roles can only view and manage tasks assigned to them. They cannot create projects or assign tasks to others.

**Deliverables:**
- Implement sign-up, login, and logout functionality.
- Implement role-based access control, ensuring that different users have different permissions based on their roles.

---

### **2. Project Management**

#### **Project Creation:**
- **Admins or Project Managers** should be able to create new projects.
- Each project should have the following attributes:
  - **Name**: The name of the project.
  - **Description**: A brief description of the project.
  - **Start Date**: The date when the project starts.
  - **End Date**: The expected completion date of the project.

#### **View Projects:**
- **Admins** should be able to view all the projects in the system.
- **Developers/Testers** should only be able to view the projects they are part of.

**Deliverables:**
- Create an API for project creation that only Admins or Project Managers can access.
- Provide a view for listing all projects, where Admins can see all projects and Developers/Testers can only see their assigned projects.

---

### **3. Task Management (Similar to JIRA Issues)**

#### **Task Types:**
- Define the following task types in the system:
  - **Bug**: Tasks that deal with fixing issues or bugs.
  - **Feature**: Tasks that involve adding new functionality.
  - **Task**: General tasks that do not fit under Bug or Feature.

Each task should include:
- **Title**: A brief title of the task.
- **Description**: A detailed explanation of the task.
- **images**: Any related documents.
- **Priority**: Priority levels (Low, Medium, High).
- **Status**: Current status of the task (Open, In Progress, Done).
- **Due Date**: The date by which the task should be completed.

#### **Task Assignment:**
- **Project Managers** should be able to assign tasks to **Developers** and **Testers**. Tasks should be linked to a specific project and assigned to individual users.

#### **Task Status:**
- Users should be able to update the status of tasks assigned to them. For example, a task status can be moved from "Open" to "In Progress" or from "In Progress" to "Done."
  
#### **Task Comments:**
- Users should have the ability to add comments to tasks for collaboration and discussion purposes.
