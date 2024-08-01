import sqlite3
import uuid
from abc import ABC, abstractmethod

# Database setup
def create_database():
    conn = sqlite3.connect('student_management.db')
    cursor = conn.cursor()
    
    # Create students table
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
    
    # Create teachers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            unique_id TEXT UNIQUE,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone_number TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Abstract base class for database operations
class DatabaseOperations(ABC):
    
    @abstractmethod
    def create(self, item):
        pass

    @abstractmethod
    def update(self, item_id, updated_item):
        pass

    @abstractmethod
    def delete(self, item_id):
        pass

    @abstractmethod
    def retrieve(self, item_id):
        pass

    @abstractmethod
    def list_items(self):
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

    def create(self, student):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO students (unique_id, first_name, last_name, date_of_birth, email, phone_number)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (student._unique_id, student.first_name, student.last_name, student.date_of_birth, student.email, student.phone_number))
        conn.commit()
        conn.close()

    def update(self, student_id, updated_student):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE students
            SET first_name = ?, last_name = ?, date_of_birth = ?, email = ?, phone_number = ?
            WHERE unique_id = ?
        ''', (updated_student.first_name, updated_student.last_name, updated_student.date_of_birth, updated_student.email, updated_student.phone_number, student_id))
        conn.commit()
        conn.close()

    def delete(self, student_id):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM students WHERE unique_id = ?
        ''', (student_id,))
        conn.commit()
        conn.close()

    def retrieve(self, student_id):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM students WHERE unique_id = ?
        ''', (student_id,))
        student = cursor.fetchone()
        conn.close()
        return student

    def list_items(self):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM students
        ''')
        students = cursor.fetchall()
        conn.close()
        return students

# Teacher class
class Teacher(DatabaseOperations):

    def __init__(self, first_name, last_name, email, phone_number):
        self._unique_id = self.generate_unique_id()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    @staticmethod
    def generate_unique_id():
        return str(uuid.uuid4())

    def create(self, teacher):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO teachers (unique_id, first_name, last_name, email, phone_number)
            VALUES (?, ?, ?, ?, ?)
        ''', (teacher._unique_id, teacher.first_name, teacher.last_name, teacher.email, teacher.phone_number))
        conn.commit()
        conn.close()

    def update(self, teacher_id, updated_teacher):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE teachers
            SET first_name = ?, last_name = ?, email = ?, phone_number = ?
            WHERE unique_id = ?
        ''', (updated_teacher.first_name, updated_teacher.last_name, updated_teacher.email, updated_teacher.phone_number, teacher_id))
        conn.commit()
        conn.close()

    def delete(self, teacher_id):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM teachers WHERE unique_id = ?
        ''', (teacher_id,))
        conn.commit()
        conn.close()

    def retrieve(self, teacher_id):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM teachers WHERE unique_id = ?
        ''', (teacher_id,))
        teacher = cursor.fetchone()
        conn.close()
        return teacher

    def list_items(self):
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM teachers
        ''')
        teachers = cursor.fetchall()
        conn.close()
        return teachers

# Main function 
def main():
    create_database()
    
    #  students
    student1 = Student("John", "Doe", "1990-01-01", "john.doe@example.com", "1234567890")
    student1.create(student1)
    student2 = Student("\nEddy", "Doe", "1990-01-01", "Eddy@gmail.com","23765242152" )
    student2.create(student2)
    student3 = Student("\nSteve", "Fotso", "1990-01-01", "Steve@gmail.com", "1234567890")
    student3.create(student3)
    
    students = student1.list_items()
    print("\nAll Students:", students)
    
    student_id = students[1][1]  
    student = student1.retrieve(student_id)
    print("\nRetrieved Student:", student)
    
    student_id2 = students[0][1]
    updated_student = Student("\nMAX", "Sender", "1990-01-01", "johnny.doe@example.com", "0987654321")
    student1.update(student_id2, updated_student)
    
    student1.delete(student_id)
    students = student1.list_items()
    print("\nAll Students after deletion:", students)
    
    #  teachers
    teacher1 = Teacher("Alice", "Smith", "alice.smith@example.com", "9876543210")
    teacher1.create(teacher1)
    teacher2 = Teacher("Bob", "Brown", "bob.brown@example.com", "5678901234")
    teacher2.create(teacher2)
    
    teachers = teacher1.list_items()
    print("\nAll Teachers:", teachers)
    
    teacher_id = teachers[0][1]
    teacher = teacher1.retrieve(teacher_id)
    print("\nRetrieved Teacher:\n", teacher)
    
    updated_teacher = Teacher("Carol", "Jones", "carol.jones@example.com", "1234567890")
    teacher1.update(teacher_id, updated_teacher)
    
    teacher1.delete(teacher_id)
    teachers = teacher1.list_items()
    print("\nAll Teachers after deletion:\n", teachers ,"\n")

if __name__ == "__main__":
    main()
