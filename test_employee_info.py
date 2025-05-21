import pytest
from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept

# Sample dataset assumed to be in employee_info.py
# Modify if needed to point to actual `employee_data`

def test_get_employees_by_age_range():
    result = get_employees_by_age_range(24, 36)
    expected_names = {"Jane", "Mary", "Chloe", "Mike"}  # Employees between age 25 and 35 (exclusive)
    result_names = {emp["name"] for emp in result}
    assert result_names == expected_names

def test_calculate_average_salary():
    average = calculate_average_salary()
    expected_average = (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6
    assert average == expected_average

def test_get_employees_by_dept():
    result = get_employees_by_dept("Marketing")
    expected_names = {"Jane", "Mary"}
    result_names = {emp["name"] for emp in result}
    assert result_names == expected_names
