import employee_info as empInfo

# Sample dataset assumed to be in employee_info.py
# Modify if needed to point to actual `employee_data`

def test_get_employees_by_age_range():
    result = empInfo.get_employees_by_age_range(25, 35)
    exp_result = [
         {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
         {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    assert (result == exp_result)

def test_calculate_average_salary():
    result = empInfo.calculate_average_salary()
    assert ( result == 60166.67)
    
def test_get_employees_by_dept():
    result = empInfo.get_employees_by_dept('Sales')
    exp_result =  [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
