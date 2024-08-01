import sqlite3
import uuid
from abc import ABC, abstractmethod

# Database setup
def create_database():
    conn = sqlite3.connect('student_management.db')
    cursor = conn.cursor()
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
    ''')
    conn.commit()
    conn.close()

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

# Student class
class Student(DatabaseOperations):

    def __init__(self, first_name, last_name, date_of_birth, email, phone_number):
        self._unique_id = self.generate_unique_id()
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number

    @staticmethod
    def generate_unique_id():
        return str(uuid.uuid4())

    def create_student(self, student):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO students (unique_id, first_name, last_name, date_of_birth, email, phone_number)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (student._unique_id, student.first_name, student.last_name, student.date_of_birth, student.email, student.phone_number))
        conn.commit()
        conn.close()

    def update_student(self, student_id, updated_student):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE students
            SET first_name = ?, last_name = ?, date_of_birth = ?, email = ?, phone_number = ?
            WHERE unique_id = ?
        ''', (updated_student.first_name, updated_student.last_name, updated_student.date_of_birth, updated_student.email, updated_student.phone_number, student_id))
        conn.commit()
        conn.close()

    def delete_student(self, student_id):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM students WHERE unique_id = ?
        ''', (student_id,))
        conn.commit()
        conn.close()

    def retrieve_student(self, student_id):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM students WHERE unique_id = ?
        ''', (student_id,))
        student = cursor.fetchone()
        conn.close()
        return student

    def list_students(self):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM students
        ''')
        students = cursor.fetchall()
        conn.close()
        return students

# Main function 
def main():
    create_database()
    
    
    student1 = Student("John", "Doe", "1990-01-01", "john.doe@example.com", "1234567890")
    student1.create_student(student1)
    student2 = Student("Eddy", "Doe", "1990-01-01", "Eddy@gmail.com","23765242152" )
    student2.create_student(student2)
    student3 = Student("Steve", "fotso", "1990-01-01", "Steve@gmail.com", "1234567890")
    student3.create_student(student3)
    
   
    students = student1.list_students()
    print("All Students:", students)
    
   
    student_id = students[1][1]  
    student = student1.retrieve_student(student_id)
    print("Retrieved Student:", student)
    
   
    updated_student = Student("Johnny", "Doe", "1990-01-01", "johnny.doe@example.com", "0987654321")
    student1.update_student(student_id, updated_student)
    
   
    student1.delete_student(student_id)
    students = student1.list_students()
    print("All Students:", students)

if __name__ == "__main__":
    main()
