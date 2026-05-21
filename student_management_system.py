"""
Student Management System
Author: Fatimah Agboola

A command-line Python application that manages student records using SQLite.
Skills demonstrated:
- Object-Oriented Programming
- SQLite database integration
- CRUD operations
- Input validation
- Report generation
"""

import sqlite3
from dataclasses import dataclass


DATABASE_NAME = "students.db"


@dataclass
class Student:
    name: str
    course: str
    grade: float


class StudentManager:
    def __init__(self, database_name: str = DATABASE_NAME):
        self.connection = sqlite3.connect(database_name)
        self.create_table()

    def create_table(self) -> None:
        with self.connection:
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    course TEXT NOT NULL,
                    grade REAL NOT NULL
                )
                """
            )

    def add_student(self, student: Student) -> None:
        with self.connection:
            self.connection.execute(
                "INSERT INTO students (name, course, grade) VALUES (?, ?, ?)",
                (student.name, student.course, student.grade),
            )
        print("Student added successfully.")

    def view_students(self) -> None:
        cursor = self.connection.execute(
            "SELECT id, name, course, grade FROM students ORDER BY id"
        )
        rows = cursor.fetchall()

        if not rows:
            print("No student records found.")
            return

        print("\nID | Name | Course | Grade")
        print("-" * 45)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

    def search_student(self, keyword: str) -> None:
        cursor = self.connection.execute(
            """
            SELECT id, name, course, grade
            FROM students
            WHERE name LIKE ? OR course LIKE ?
            """,
            (f"%{keyword}%", f"%{keyword}%"),
        )
        rows = cursor.fetchall()

        if not rows:
            print("No matching records found.")
            return

        print("\nSearch Results")
        print("-" * 45)
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Course: {row[2]} | Grade: {row[3]}")

    def update_grade(self, student_id: int, new_grade: float) -> None:
        with self.connection:
            cursor = self.connection.execute(
                "UPDATE students SET grade = ? WHERE id = ?",
                (new_grade, student_id),
            )

        if cursor.rowcount == 0:
            print("Student ID not found.")
        else:
            print("Grade updated successfully.")

    def delete_student(self, student_id: int) -> None:
        with self.connection:
            cursor = self.connection.execute("DELETE FROM students WHERE id = ?", (student_id,))

        if cursor.rowcount == 0:
            print("Student ID not found.")
        else:
            print("Student deleted successfully.")

    def generate_report(self) -> None:
        cursor = self.connection.execute(
            "SELECT COUNT(*), AVG(grade), MAX(grade), MIN(grade) FROM students"
        )
        count, average, highest, lowest = cursor.fetchone()

        if count == 0:
            print("No data available for report.")
            return

        print("\nStudent Performance Report")
        print("-" * 45)
        print(f"Total Students: {count}")
        print(f"Average Grade: {average:.2f}")
        print(f"Highest Grade: {highest:.2f}")
        print(f"Lowest Grade: {lowest:.2f}")

    def close(self) -> None:
        self.connection.close()


def get_float_input(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value < 0 or value > 100:
                print("Grade must be between 0 and 100.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid ID number.")


def main() -> None:
    manager = StudentManager()

    while True:
        print("\nStudent Management System")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update grade")
        print("5. Delete student")
        print("6. Generate report")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Student name: ").strip()
            course = input("Course: ").strip()
            grade = get_float_input("Grade (0-100): ")

            if not name or not course:
                print("Name and course cannot be empty.")
                continue

            manager.add_student(Student(name, course, grade))

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            keyword = input("Enter name or course to search: ").strip()
            manager.search_student(keyword)

        elif choice == "4":
            student_id = get_int_input("Enter student ID: ")
            new_grade = get_float_input("Enter new grade (0-100): ")
            manager.update_grade(student_id, new_grade)

        elif choice == "5":
            student_id = get_int_input("Enter student ID: ")
            manager.delete_student(student_id)

        elif choice == "6":
            manager.generate_report()

        elif choice == "7":
            manager.close()
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 7.")


if __name__ == "__main__":
    main()
