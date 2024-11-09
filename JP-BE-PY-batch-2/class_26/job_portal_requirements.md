### Project Overview 

---

### 1. **Authentication**
   - **Sign Up** (`POST /auth/signup`)
     - **Email verification required**: Upon signup, send a verification email.
   - **Login** (`POST /auth/login`)
   - **Change Password** (`PUT /auth/change-password`)
   - **Forgot Password** (`POST /auth/forgot-password`)
     - **Email verification required**: Send a password reset link via email.
   - **Forgot Password** (`POST /auth/forgot-password/email-verification`)

---

### 2. **User Profiles**

#### **Job Seeker Profile**
   - **Fields**: First Name, Last Name, Email, Gender, Date of Birth, Qualification, CV, Country, City, Profile Image.
   - **Create/Update Profile** (`POST /profile/job-seeker`, `PUT /profile/job-seeker`)

#### **Employer Profile**
   - **Fields**: First Name, Last Name, Email, Gender, Date of Birth, Company Name, Country, City, Company Size, Logo.
   - **Create/Update Profile** (`POST /profile/employer`, `PUT /profile/employer`)

---

### 3. **Job Posts**

#### **Job Listings**
   - **Guest Access** (`GET /jobs`): 20 latest jobs with search filters and pagination.
   - **Logged-In Access**: Additional fields like salary range and apply button for job seekers.

#### **Job Profile**
   - **Endpoint**: `GET /jobs/<id>`
   - **Fields**: Company logo, company name, job title, job description, location, salary range (for logged-in users), company info, and apply button.

#### **Company Job Management**
   - **Create Job Post** (`POST /jobs`)
   - **View Employer’s Own Posts** (`GET /jobs/my-jobs`)
   - **Update Job Post** (`PUT /jobs/<id>`)
   - **Toggle Job Post Status** (`PUT /jobs/<id>/toggle`)
   - **View Applicants for Job Post** (`GET /jobs/<id>/applicants`)
   - **Update Applicant Status** (`PUT /jobs/<id>/applicants/<applicant_id>/status`)

---

### 4. **Applications and Notifications**

#### **Job Applications (Job Seekers)**
   - **Apply to Job** (`PUT /jobs/<id>/apply`)
   - **View My Applications** (`GET /jobs/my-applications`)

#### **Notifications**
   - **Job Seeker Notifications** (`GET /notifications`)
   - **Employer Notifications** (`GET /notifications`)

---

### 5. **Admin Interface**

   - **Approve Company** (`GET /company/<id>/approve`)
   - **Approve Job Post** (`PUT /admin/job-post/<id>/approve`)

---

### 6. **Guest Access**

#### **Homepage (`GET /`)**
   - **20 Latest Jobs**: Displays the latest 20 jobs.
   - **Search Filters**: City, country, job type, and company name.

---

### 7. **Metrics APIs**

#### **Employer Metrics**
These APIs help employers track the performance of their job postings.

   - **Get Active Job Metrics** (`GET /employer/metrics/active-jobs`)
     - **Description**: Shows metrics for jobs currently active.
     - **Fields**:
       - Total Active Job Posts
       - Total Applications for Active Jobs
       - Total Hired from Active Jobs

   - **Get Overall Job Metrics** (`GET /employer/metrics/overall-jobs`)
     - **Description**: Shows metrics for all jobs, including disabled posts.
     - **Fields**:
       - Total Job Posts (including disabled)
       - Total Applications (all jobs)
       - Total Hired Across All Jobs

   - **Get Job-Specific Metrics** (`GET /employer/metrics/job/<job_id>`)
     - **Description**: Provides metrics specific to a single job post.
     - **Fields**:
       - Number of Applicants
       - Number Approved
       - Number Hired

#### **Job Seeker Metrics**
These APIs provide job seekers with insights into their job application journey.

   - **Get Application Summary** (`GET /job-seeker/metrics/applications`)
     - **Description**: Provides an overview of all applications by the job seeker.
     - **Fields**:
       - Total Applications Submitted
       - Number of Active Applications (for jobs still enabled)
       - Number of Rejected Applications
       - Number of Approved Applications
       - Number of Hired Status

   - **Get Application Status Breakdown** (`GET /job-seeker/metrics/applications/status`)
     - **Description**: Breaks down applications by status.
     - **Fields**:
       - Number of Applications Pending
       - Number of Applications Approved
       - Number of Applications Rejected
       - Number of Applications Hired

   - **Get Application Activity Over Time** (`GET /job-seeker/metrics/applications/activity`)
     - **Description**: Displays a timeline or activity chart of applications over the past months.
     - **Fields**:
       - Number of Applications Submitted (monthly breakdown)
       - Number Approved Over Time
       - Number Hired Over Time

