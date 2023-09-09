"""
In this exercise, you will create a Python class named Student to represent students. 
The class should have the following attributes and methods:

Attributes:

name: instance variable
age: instance variable
courses: instance variable
available_courses: class variable -> possible values ["English", "Urdu", "Physics", "Math", "Chemistry"]

Methods:

display_info(): An instance method that displays the student's name and age.
enroll(): An instance method that allows a student to enroll in a course by adding it to their list of enrolled courses.
list_courses(): An instance method that displays all the courses that student is enrolled
list_available_courses(): An instance method that display all the avaiable courses


1. Create three instances of the Student class with different names and ages.

2. enroll the students in courses by calling the enroll method.
make sure student should only enroll in the course that are listing in available course
i.e if user input the course "Islamyat" then program should not allow it

3. call list_courses
4. call list_available_courses
"""
