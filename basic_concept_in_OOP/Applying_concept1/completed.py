import sqlite3
import uuid
from abc import ABC, abstractmethod

# Function to create the SQLite3 database and student table if they do not exist
def create_database():
    conn = sqlite3.connect('student_management.db')  # Connect to the database
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            unique_id TEXT UNIQUE,
            first_name TEXT,
            last_name TEXT,
            date_of_birth TEXT,
            email TEXT,
            phone_number TEXT
        )
    ''')  # SQL query to create the students table
    conn.commit()  # Commit the changes
    conn.close()  # Close the connection

# Abstract base class for database operations
class DatabaseOperations(ABC):

    @abstractmethod
    def create_student(self, student):
        pass

    @abstractmethod
    def update_student(self, student_id, updated_student):
        pass

    @abstractmethod
    def delete_student(self, student_id):
        pass

    @abstractmethod
    def retrieve_student(self, student_id):
        pass

    @abstractmethod
    def list_students(self):
        pass

# Student class inheriting from DatabaseOperations
class Student(DatabaseOperations):

    def __init__(self, first_name, last_name, date_of_birth, email, phone_number):
        self.conn = sqlite3.connect('student_management.db')  # Connect to the database
        self.cursor = self.conn.cursor()  # Create a cursor object
        self._unique_id = self.generate_unique_id()  # Generate unique ID
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number

    @staticmethod
    def generate_unique_id():
        return str(uuid.uuid4())  # Generate a UUID for unique ID

    # Method to insert a new student into the database
    def create_student(self, student):
        self.cursor.execute('''
            INSERT INTO students (unique_id, first_name, last_name, date_of_birth, email, phone_number)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (student._unique_id, student.first_name, student.last_name, student.date_of_birth, student.email, student.phone_number))  # SQL query to insert a student
        self.conn.commit()  # Commit the changes

    # Method to update an existing student's details in the database
    def update_student(self, student_id, updated_student):
        # Retrieve the current student information
        current_student = self.retrieve_student(student_id)
        if not current_student:
            print("Student not found!")
            return
        
        print("Current Student Details:")
        print(f"ID: {current_student[1]}")
        print(f"First Name: {current_student[2]}")
        print(f"Last Name: {current_student[3]}")
        print(f"Date of Birth: {current_student[4]}")
        print(f"Email: {current_student[5]}")
        print(f"Phone Number: {current_student[6]}")

        confirm = input("Is this the student you want to update? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Update cancelled.")
            return

        # Ask for new information and retain the old information if not provided
        first_name = input(f"Enter New First Name [{current_student[2]}]: ") or current_student[2]
        last_name = input(f"Enter New Last Name [{current_student[3]}]: ") or current_student[3]
        date_of_birth = input(f"Enter New Date of Birth (YYYY-MM-DD) [{current_student[4]}]: ") or current_student[4]
        email = input(f"Enter New Email [{current_student[5]}]: ") or current_student[5]
        phone_number = input(f"Enter New Phone Number [{current_student[6]}]: ") or current_student[6]

        self.cursor.execute('''
            UPDATE students
            SET first_name = ?, last_name = ?, date_of_birth = ?, email = ?, phone_number = ?
            WHERE unique_id = ?
        ''', (first_name, last_name, date_of_birth, email, phone_number, student_id))  # SQL query to update a student
        self.conn.commit()  # Commit the changes
        print("Student updated successfully!")

    # Method to delete a student from the database
    def delete_student(self, student_id):
        # Retrieve the current student information
        current_student = self.retrieve_student(student_id)
        if not current_student:
            print("Student not found!")
            return
        
        print("Current Student Details:")
        print(f"ID: {current_student[1]}")
        print(f"First Name: {current_student[2]}")
        print(f"Last Name: {current_student[3]}")
        print(f"Date of Birth: {current_student[4]}")
        print(f"Email: {current_student[5]}")
        print(f"Phone Number: {current_student[6]}")

        confirm = input("Is this the student you want to delete? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Delete cancelled.")
            return

        self.cursor.execute('''
            DELETE FROM students WHERE unique_id = ?
        ''', (student_id,))  # SQL query to delete a student
        self.conn.commit()  # Commit the changes
        print("Student deleted successfully!")

    # Method to retrieve a student's details from the database
    def retrieve_student(self, student_id):
        self.cursor.execute('''
            SELECT * FROM students WHERE unique_id = ?
        ''', (student_id,))  # SQL query to retrieve a student
        student = self.cursor.fetchone()  # Fetch the student's details
        return student  # Return the student's details

    # Method to list all students in the database
    def list_students(self):
        self.cursor.execute('''
            SELECT * FROM students
        ''')  # SQL query to list all students
        students = self.cursor.fetchall()  # Fetch all students
        return students  # Return the list of students

    # Method to close the database connection
    def close_connection(self):
        self.conn.close()  # Close the connection

# Function to display the menu and handle user input
def main():
    create_database()  # Ensure the database and table are created

    while True:
        print("\nStudent Management System")
        print("1. Create Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Retrieve Student")
        print("5. List Students")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")
            email = input("Enter Email: ")
            phone_number = input("Enter Phone Number: ")
            student = Student(first_name, last_name, date_of_birth, email, phone_number)
            student.create_student(student)
            print("Student created successfully!")
            student.close_connection()  # Close the connection

        elif choice == '2':
            student_id = input("Enter Student Unique ID to Update: ")
            student = Student("", "", "", "", "")
            student.update_student(student_id, student)
            student.close_connection()  # Close the connection

        elif choice == '3':
            student_id = input("Enter Student Unique ID to Delete: ")
            student = Student("", "", "", "", "")
            student.delete_student(student_id)
            student.close_connection()  # Close the connection

        elif choice == '4':
            student_id = input("Enter Student Unique ID to Retrieve: ")
            student = Student("", "", "", "", "")
            retrieved_student = student.retrieve_student(student_id)
            if retrieved_student:
                print("Student Details:")
                print(f"ID: {retrieved_student[1]}")
                print(f"First Name: {retrieved_student[2]}")
                print(f"Last Name: {retrieved_student[3]}")
                print(f"Date of Birth: {retrieved_student[4]}")
                print(f"Email: {retrieved_student[5]}")
                print(f"Phone Number: {retrieved_student[6]}")
            else:
                print("Student not found!")
            student.close_connection()  # Close the connection

        elif choice == '5':
            student = Student("", "", "", "", "")
            students = student.list_students()
            print("All Students:")
            for s in students:
                print(f"ID: {s[1]}, Name: {s[2]} {s[3]}, DOB: {s[4]}, Email: {s[5]}, Phone: {s[6]}")
            student.close_connection()  # Close the connection

        elif choice == '6':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()  # Call the main function to run the program
