student_data = [
    {"name": "Alice", "grades": {"Math": 85, "English": 90, "Science": 78}},
    {"name": "Bob", "grades": {"Math": 65, "English": 72, "Science": 68}},
    {"name": "Charlie", "grades": {"Math": 95, "English": 92, "Science": 88}},
    {"name": "Diana", "grades": {"Math": 55, "English": 60, "Science": 65}},
]

def get_average_grade(student_name):
    for student in student_data:
        if student["name"] == student_name:
            grades = student["grades"].values()
            average = sum(grades) / len(grades)
            return round(average, 2)
    return None  # Return None if student not found

def get_students_above_threshold(subject, threshold):
    result = []
    for student in student_data:
        if subject in student["grades"] and student["grades"][subject] > threshold:
            result.append(student["name"])
    return result

def calculate_class_average(subject):
    total = 0
    count = 0
    for student in student_data:
        if subject in student["grades"]:
            total += student["grades"][subject]
            count += 1
    if count == 0:
        return None
    return round(total / count, 2)
