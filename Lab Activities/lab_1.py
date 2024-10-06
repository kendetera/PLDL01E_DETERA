# gathering of inputs
student_name = input("Enter student name: ")
quizzes = float(input("Enter final quizzes rating: "))
research = float(input("Enter final research/assignment rating: "))
project = float(input("Enter final project rating: "))
exam = float(input("Enter final exam rating: "))

# formula
final_grade = 0.30 * quizzes + 0.10 * research + 0.40 * exam + 0.20 * project

# calculation
if final_grade > 100:
    remark = "No grade should exceed 100!"
elif 98 <= final_grade <= 100:
    remark = 4.00
elif 95 <= final_grade <= 97:
    remark = 3.75
elif 92 <= final_grade <= 94:
    remark = 3.50
elif 89 <= final_grade <= 91:
    remark = 3.25
elif 86 <= final_grade <= 88:
    remark = 3.00
elif 83 <= final_grade <= 85:
    remark = 2.75
elif 80 <= final_grade <= 82:
    remark = 2.50
elif 77 <= final_grade <= 79:
    remark = 2.25
elif 74 <= final_grade <= 76:
    remark = 2.00
elif 71 <= final_grade <= 73:
    remark = 1.75
elif 68 <= final_grade <= 70:
    remark = 1.50
elif 64 <= final_grade <= 67:
    remark = 1.25
elif 60 <= final_grade <= 63:
    remark = 1.00
elif final_grade < 60:
    remark = 0.00
else:
    remark = None

# displaying of outputs
print("Student name: ", student_name)
print("Final quizzes: ", quizzes)
print("Final research/assignment: ", research)
print("Final project: ", project)
print("Final exam: ", exam)
print("Final Grade: ", final_grade)
print("Equivalent remark:", remark)
