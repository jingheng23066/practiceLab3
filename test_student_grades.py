import student_grades as sg

def test_get_average_grade():
    # Write the test code here
    result = sg.get_average_grade("Alice")
    expected_result = 84.33
    assert result == expected_result

def test_get_students_above_threshold():
    # Write the test code here
    assert set(sg.get_students_above_threshold("Math", 70)) == {"Alice", "Charlie"}

    
def test_calculate_class_average():
    assert sg.calculate_class_average("Math") == 75.0  # Write the test code here
