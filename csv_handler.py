"""""
CSV Student Grade Manager
Professional file I/O with error handling and type hints
"""

import csv
import json
import os
from typing import List, Dict

def read_csv(filename: str) -> List[Dict[str, str]]:
    """
    Read CSV file and return list of dictionaries.
    Args:
    filename: Path to CSV file
    Returns:
    List of dictionaries with student data
    Raises:
    FileNotFoundError: If file doesn't exist
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} not found")
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

def update_csv_student(filename: str, name: str, new_grade: int) -> None:
    """
    Update a student's grade in CSV file.
    Args:
    filename: Path to CSV file
    name: Student name to find
    new_grade: New grade value
    """
    rows = read_csv(filename)
    updated = False
    for row in rows:
        if row['name'] == name:
            row['grade'] = str(new_grade)
            updated = True
        if not updated:
            print(f"Student '{name}' not found")
            return
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'course', 'grade'])
        writer.writeheader()
        writer.writerows(rows)
        print(f"Updated {name} to grade {new_grade}")

def read_json(filename: str) -> List[Dict]:
    """
    Read JSON file and return list of dictionaries.
    Args:
    filename: Path to JSON file
    Returns:
    List of dictionaries with student data
    Raises:
    FileNotFoundError: If file doesn't exist
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} not found")
    with open(filename, 'r') as f:
        return json.load(f)

def update_json_student(filename: str, name: str, new_grade: int) -> None:
    """
    Update a student's grade in JSON file.
    Args:
    filename: Path to JSON file
    name: Student name to find
    new_grade: New grade value
    """
    data = read_json(filename)
    updated = False
    for student in data:
        if student['name'] == name:
            student['grade'] = new_grade
            updated = True
    if not updated:
        print(f"Student '{name}' not found")
        return
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        print(f"Updated {name} to grade {new_grade}")


def add_new_student_csv(filename: str, name: str, course: str, grade: int) -> None:
    with open(filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'course', 'grade'])
        writer.writerow({'name': name, 'course': course, 'grade': grade})

    

print("\n--- Testing CSV Functions ---")
print("Before:", read_csv('data/students.csv'))
update_csv_student('data/students.csv', 'Alice', 90)
print("After:", read_csv('data/students.csv'))
print("\n--- Testing JSON Functions ---")
print("Before:", read_json('data/students.json'))
update_json_student('data/students.json', 'Bob', 98)
print("After:", read_json('data/students.json'))
print("\n--- Adding New Student to CSV ---")
add_new_student_csv('data/students.csv', 'Dana', 'Python', 88)
print("After: ", read_csv('data/students.csv'))