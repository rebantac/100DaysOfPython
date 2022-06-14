
student_marks = input("Enter Student Marks: ").split()
print(student_marks)

max = 0

for student_mark in student_marks:
    student_mark = int(student_mark)
    if max < student_mark:
        max = student_mark

print("Highest Mark: ", max)