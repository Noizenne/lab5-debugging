"""
BUGGY PROGRAM - Find and fix 3 bugs using VS Code debugger!
This should calculate average grade from CSV file
"""
import csv
from fileinput import filename
def buggy_average(filename):
    """Calculate average grade - BUT IT HAS BUGS!"""
    rows = []
    # BUG 1: Using wrong CSV reader
    with open(filename, 'r') as f:
        reader = csv.DictReader(f) # Should be DictReader!
        rows = list(reader)
        total = 0
        count = 0
        for row in rows: # Skip header row
            name = row['name']
            course = row['course']
            # BUG 2: Wrong column index for grade
            grade_str = row['grade'] # Grade is at index 2, not 3!
            grade = float(grade_str)
            total += grade
            count += 1
            print(f"{name}: {grade}")
            # BUG 3: Division by zero if no students
            # (This is actually prevented by rows[1:], but still bad practice)
        if count == 0:
            print("No students found.")
            return 0.0
        avg = total / count 
        print(f"\nAverage: {avg}")
        return avg      
result = buggy_average('data/students.csv')