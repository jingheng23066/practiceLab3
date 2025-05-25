student_records = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [70, 60, 75]},
    {"name": "Charlie", "grades": [95, 92, 88]},
    {"name": "Diana", "grades": [55, 65, 60]}
]

def get_average_grade(student_name):
    for student in student_records:
        if student["name"] == student_name:
            return round(sum(student["grades"]) / len(student["grades"]), 2)
    return None

def get_top_student():
    top_student = None
    highest_avg = 0
    for student in student_records:
        avg = sum(student["grades"]) / len(student["grades"])
        if avg > highest_avg:
            highest_avg = avg
            top_student = student["name"]
    return top_student

def get_students_below_average(class_avg):
    result = []
    for student in student_records:
        avg = sum(student["grades"]) / len(student["grades"])
        if avg < class_avg:
            result.append(student["name"])
    return result

def calculate_class_average():
    total = 0
    count = 0
    for student in student_records:
        total += sum(student["grades"])
        count += len(student["grades"])
    return round(total / count, 2)


