"""
Math utilities for grade calculations
These functions will be tested with pytest
"""
from typing import List
def average_grades(grades: List[float]) -> float:
    """
    Calculate average of grades.
    Args:
    grades: List of grade values
    Returns:
    Average grade, 0.0 if empty list
    """
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

def pass_rate(grades: List[float], threshold: float = 70.0) -> float:
    """
    Calculate percentage of grades above threshold.
    Args:
    grades: List of grade values
    threshold: Minimum passing grade (default 70.0)
    Returns:
    Percentage of passing grades (0-100)
    """
    if not grades:
        return 0.0
    passing = sum(1 for g in grades if g >= threshold)
    return (passing / len(grades)) * 100

def letter_grade(score: float) -> str:
    """
    Convert numeric grade to letter grade.
    Args:
    score: Numeric grade (0-100)
    Returns:
    Letter grade (A, B, C, D, F)
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'