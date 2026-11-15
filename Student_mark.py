
from __future__ import print_function

# Support both Python 2 and Python 3
try:
    read_input = raw_input
except NameError:
    read_input = input


print("===== STUDENT MARKS MANAGEMENT SYSTEM =====")

# Get student name
student_name = read_input("Enter student name: ")

# Subject names
subjects = ["Tamil", "English", "Maths", "Physics", "Chemistry"]

# Store marks
marks = []

# Get marks from student
for subject in subjects:

    while True:
        try:
            mark = float(read_input("Enter " + subject + " marks: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


# Calculate total and average
total = sum(marks)
average = total / float(len(marks))


# Calculate grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "E"


# Display student report
print("\n===== STUDENT REPORT =====")

print("Student Name:", student_name)

for subject, mark in zip(subjects, marks):
    print(subject + ":", mark)

print("Total Marks:", total, "/ 500")
print("Average:", average)
print("Grade:", grade)

print("==========================")
