### Job Fair Application - Updated Functional Requirements

#### 1. User Roles:
- **Admin**: Has access to Django's admin interface and can view and manage the platform's overall activity, including approved job seekers associated with each employer.
- **Employer**: Can register, create and manage job posts, review applicants, approve or reject job applications, and mark job seekers as "hired."
- **Job Seeker**: Can register, view and apply for jobs, and track the status of their applications.

#### 2. Employer Features:
1. **Employer Registration/Login**:
   - Employers can register with details like company name, email, password, and company description.
   - After registering, employers can log in to access their dashboard.

2. **Create Job Posts**:
   - Employers can create job postings by providing details such as job title, description, required skills, and salary range.
   - Job posts can be enabled/disabled (disabled posts are hidden from job seekers).
   - Employers can view all job posts they have created.

3. **Manage Applications**:
   - Employers can view all job seekers who applied to their job posts.
   - For each applicant, employers can view the job seeker’s profile, which includes name, contact info, and CV.
   - Employers can approve or reject applications:
     - **Approve**: Indicates the job seeker is moving forward in the hiring process.
     - **Reject**: Ends the application process for that job.
   - Employers can mark approved job seekers as "hired" once they have completed the interview and onboarding process.

4. **View All Jobs and Applications**:
   - Employers can view all their job postings and track application statuses (approved for interview, rejected, or hired).

#### 3. Job Seeker Features:
1. **Job Seeker Registration/Login**:
   - Job seekers can register with personal details such as name, email, password, and CV.
   - Job seekers must log in to apply for jobs.

2. **View Job Posts**:
   - Job seekers (even those not logged in) can view a list of available job posts, including job title, description, and company.

3. **Apply to Jobs (after Login)**:
   - Logged-in job seekers can apply for jobs by clicking the "Apply" button.
   - Job seekers cannot apply for the same job twice.

4. **View Application Status**:
   - Job seekers can view the status of their applications (approved, rejected, or hired).

#### 4. Admin Features:
1. **Access Django Admin Interface**:
   - The admin user can access Django’s admin dashboard to manage platform data.

2. **View Approved Job Seekers**:
   - The admin can view all approved job seekers under each company's profile in the Django admin dashboard. This will allow the admin to track hiring progress for each employer and job seeker.


### Task Breakdown:

1. **Create Database Schema**
   - Define a database schema to support the following entities:
     - Admin: Manages the application.
     - Employer: Registers, manages job posts, and reviews applications.
     - Job Seeker: Registers, views job posts, applies to jobs, and tracks application status.
   - Ensure the schema includes fields for job details, employer information, and job seeker application status.

2. **Export Database Schema as ERD**
   - Use an ERD (Entity-Relationship Diagram) tool to visualize the database schema.
   - The ERD should clearly show relationships among entities like Admin, Employer, Job Seeker, Job Post, and Application Status.

3. **Document Required APIs**
   - Create a document listing all the APIs required for this application.
   - Describe each API endpoint, including the method, endpoint URL, and a brief description of its purpose.

4. **Document API Input and Output Formats**
   - For each API, specify the expected input and output formats.
   - Example API definitions:

---

### API Definitions (Sample)

- **User Authentication**
    - **POST /auth/login**
      - **Request:**
        ```json
        {
          "username": "string",
          "password": "string"
        }
        ```
      - **Response:**
        ```json
        "success"
        ```

    - **POST /auth/signup** 
      - **Request:**
        ```json
        {
          "username": "string",
          "password": "string"
        }
        ```
      - **Response:**
        ```json
        "success"
        ```

- **Job Listings**
    - **GET /jobs**
      - **Description:** Displays all available job posts.
      - **Response:**
        ```json
        [
          {
            "title": "string",
            "description": "string",
            "company_name": "string"
          }
        ]
        ```

    - **GET /employer/jobs**
      - **Description:** Displays job posts specific to the logged-in employer.
      - **Response:**
        ```json
        [
          {
            "title": "string",
            "description": "string"
          }
        ]
        ```
