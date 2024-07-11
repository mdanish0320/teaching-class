# create a text file and add the below content without quotation marsk
"""
Hi *user*!

We've found the best article for you based on your interest: *title*
Please click *here* to open the article
"""

# task is to read the above file and update the placeholder i.e *user*, *title* and *here*
# and store the updated content in user_email.txt
# run program three times with different name, title and link

# after running the program three times
# the file user_email.txt must have all three users content


# Create a new text file named "student_records.txt" with the following initial content:
# Student ID | Student Name | Grade
# 101       | Alice        | A
# 102       | Bob          | B
# 103       | Carol        | C

# Open the "student_records.txt" file in read mode ('r') and read its contents line by line. Print each line to the console.

# Create a new text file named "updated_records.txt" in write mode('w').
# Read the content of "student_records.txt" again and write only the lines containing students with grades 'A' or 'B' to the "updated_records.txt" file.
# Close both files.

# Open "updated_records.txt" in append mode('a') and add a new student record:
# Close the "updated_records.txt" file.

# Open "updated_records.txt" in read mode and print its contents to the console to verify that the new student record has been added.




#########################
#########################
#########################

"""
### Assignment: Password Manager Program
Demo: https://www.youtube.com/watch?v=O8596GPSJV4

#### Objective:
Create a password manager program that allows users to store, retrieve, and manage their passwords. 
The program will use file handling to save and read data, and it will be run in the terminal.

#### Requirements:
1. **File Handling**: Store the passwords in a file. Each entry should include the website, username, and password.
2. **Input Function**: Allow users to add new passwords, retrieve existing passwords, and delete passwords.
3. **Basic Operations**:
    - **Add a new password**: Ask for the website, username, and password. Save this information to the file.
    - **Retrieve a password**: Ask for the website and return the username and password.
    - **Delete a password**: Ask for the website and remove the corresponding entry from the file.
4. **Basic Error Handling**: Handle cases where the website is not found when retrieving or deleting a password and also when file doesn't exists

#### Program Flow:
1. Display a menu with the following options:
    - Add a new password
    - Retrieve a password
    - Delete a password
    - Exit
2. Based on the user's choice, perform the corresponding operation.
3. Repeat the menu until the user chooses to exit.

#### Detailed Instructions:
1. **Menu Display**: Create a function to display the menu and get the user's choice.
2. **Add Password**:
    - Prompt the user for the website, username, and password.
    - Write this information to a file in a structured format.
3. **Retrieve Password**:
    - Prompt the user for the website.
    - Read the file and find the entry for the given website.
    - Display the username and password.
4. **Delete Password**:
    - Prompt the user for the website.
    - Read the file and find the entry for the given website.
    - Remove the entry and update the file.
5. **File Format**: Store each entry in a new line in the format:
    ```
    website,username,password
    ```

#### Example:
1. **Add Password**:
    ```
    Enter website: example.com
    Enter username: user1
    Enter password: pass123
    Password saved successfully!
    ```
2. **Retrieve Password**:
    ```
    Enter website: example.com
    Username: user1
    Password: pass123
    ```
3. **Delete Password**:
    ```
    Enter website: example.com
    Password deleted successfully!
    ```

#### Hints:
- Use functions to keep your code organized.
- Use lists and dictionaries to manage the data in memory before writing to or reading from the file.
- Ensure to handle cases where the file may not exist initially.

#### Additional Notes:
- Focus on functionality rather than security for this assignment.
"""

"""
create the same program again but this time file data should be stored in json
"""

"""
create the same program again but this time file data should be stored in binary using pickle module
"""


"""
An email with placeholders for user details that need to be formatted.
An email subject in all lowercase that needs to be converted to uppercase.
An email body in all uppercase that needs to be converted to lowercase.
An email with a sentence that needs to have the first letter capitalized.
An email subject that needs to be converted to title case.
An email body with leading and trailing spaces that need to be removed.
An email with a repeated word that needs to be replaced.
An email that needs to find the position of a keyword.
An email body that needs to be split into a list of words.
An email with a list of words that need to be joined into a single sentence.


emails.txt
Email 1:
Hello, {name}! Your account has been {status}.

Email 2:
subject: meeting reminder
body: Don't forget about the meeting tomorrow.

Email 3:
subject: IMPORTANT UPDATE
body: PLEASE REVIEW THE ATTACHED DOCUMENT.

Email 4:
subject: follow up
body: this email needs to be capitalized.

Email 5:
subject: weekly update
body: Here is your weekly update on the project status.

Email 6:
subject:  Feedback
body:    Thank you for your feedback. Please respond at your earliest convenience.    

Email 7:
subject: error report
body: The system encountered an error error that needs to be addressed.

Email 8:
subject: keyword search
body: Please find the keyword 'search' in this email.

Email 9:
subject: word split
body: Split this email into individual words.

Email 10:
subject: words join
body: join these words into a single sentence
"""

