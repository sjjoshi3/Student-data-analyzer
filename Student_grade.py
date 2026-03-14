# Student Data Analyzer

student_marks = {}

while True:

    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    student_marks[name] = marks

    choice = input("Add another student? (y/n): ")

    if choice.lower() == 'n':
        break


# Analysis
highest_marks = max(student_marks.values())
topper = max(student_marks, key=student_marks.get)

lowest_marks = min(student_marks.values())
lowest_student = min(student_marks, key=student_marks.get)

average_marks = sum(student_marks.values()) / len(student_marks)

print("\n----- CLASS REPORT -----")

print(f"Topper : {topper} ({highest_marks})")
print(f"Lowest : {lowest_student} ({lowest_marks})")
print(f"Average : {average_marks}")
print(f"Total Students : {len(student_marks)}")


# Grade function
def grade_finder(marks):

    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


print("\n----- STUDENT REPORT -----")

for name, marks in student_marks.items():
    print(f"{name} : {marks} → Grade {grade_finder(marks)}")