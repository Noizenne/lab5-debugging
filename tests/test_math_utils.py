"""
Tests for math_utils.py functions
Run with: pytest tests/test_math_utils.py -v
"""
import pytest
from math_utils import average_grades, pass_rate, letter_grade

def test_average_grades_empty():
    """Empty list should return 0.0"""
    assert average_grades([]) == 0.0

def test_average_grades_single():
    """Single grade should return that grade"""
    assert average_grades([85.0]) == 85.0

def test_average_grades_normal():
    """Normal case with multiple grades"""
    assert average_grades([85, 92, 78]) == 85.0

@pytest.mark.parametrize("grades,expected", [
([100], 100.0),
([0, 100], 50.0),
([85.5, 90.5], 88.0),
([70, 80, 90], 80.0)
])
def test_average_parametrized(grades, expected):
    """Parametrized test for multiple cases"""
    assert average_grades(grades) == expected

def test_pass_rate_all_pass():
    """All students passing"""
    assert pass_rate([85, 90, 75]) == 100.0
def test_pass_rate_some_pass():
    """Some students passing"""
    result = pass_rate([85, 60, 92])
    assert abs(result - 66.67) < 0.1 # 2/3 passing
def test_pass_rate_custom_threshold():
    """Custom passing threshold"""
    result = pass_rate([85, 60, 92], threshold=90.0)
    assert abs(result - 33.33) < 0.1 # 1/3 passing
def test_pass_rate_empty():
    """Empty list should return 0.0"""
    assert pass_rate([]) == 0.0

@pytest.mark.parametrize("score,expected", [
(95, 'A'), (90, 'A'), (89, 'B'), (85, 'B'),
(80, 'B'), (79, 'C'), (75, 'C'), (70, 'C'),
(69, 'D'), (65, 'D'), (60, 'D'), (59, 'F'),
(0, 'F')
])

def test_letter_grade(score, expected):
    """Test all letter grade boundaries"""
    assert letter_grade(score) == expected    