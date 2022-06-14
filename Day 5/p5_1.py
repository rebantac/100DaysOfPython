
student_heights = input("Enter Student Heights: ").split()
print(student_heights)

sum_heights = 0
number_student = 0

for student_height in student_heights:
    student_height = int(student_height)
    sum_heights += student_height
    number_student += 1

print(student_heights)
print("Average height: ", round(sum_heights/number_student))