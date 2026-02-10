"""
Tests for CSV/JSON file operations
"""
from csv_handler import read_csv, read_json, update_csv_student

def test_csv_read():
    """Test reading CSV file"""
    students = read_csv('data/students.csv')
    assert len(students) >= 3
    assert students[0]['name'] in ['Alice', 'Bob', 'Charlie']
def test_csv_update():
    """Test updating CSV student grade"""
    update_csv_student('data/students.csv', 'Charlie', 78)
    students = read_csv('data/students.csv')
    charlie = next(s for s in students if s['name'] == 'Charlie')
    assert int(charlie['grade']) == 78
def test_json_read():
    """Test reading JSON file"""
    students = read_json('data/students.json')
    assert len(students) >= 3
    assert isinstance(students[0]['grade'], int)