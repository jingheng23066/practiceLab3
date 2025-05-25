import student_info as stuInfo

def test_get_average_grade():
    assert stuInfo.get_average_grade("Alice") == 84.33
    assert stuInfo.get_average_grade("Bob") == 68.33
    assert stuInfo.get_average_grade("Charlie") == 91.67
    assert stuInfo.get_average_grade("Diana") == 60.0
    assert stuInfo.get_average_grade("Unknown") is None  # Test non-existent student

def test_get_top_student():
    result = stuInfo.get_top_student()
    assert result == "Charlie"

def test_calculate_class_average():
    result = stuInfo.calculate_class_average()
    assert result == 76.08

def test_get_students_below_average():
    class_avg = stuInfo.calculate_class_average()  # ❌ You forgot the () to call the function
    result = stuInfo.get_students_below_average(class_avg)
    assert set(result) == {"Bob", "Diana"}

