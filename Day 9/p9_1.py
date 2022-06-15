student_scores = {
    "Harry": 81,
    "Ron" : 78,
    "Hermoine": 99,
    "Draco" : 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    grade = ""

    if student_scores[key] > 90:
        grade = "Outstanding"
    elif student_scores[key] > 80:
        grade = "Exceeds Expectations"
    elif student_scores[key] > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[key] = grade



print(student_grades)