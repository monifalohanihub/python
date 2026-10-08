students = {
    101: {
        "name": "Ram",
        "age": 20,
        "course": "Python"
    },
    102: {
        "name": "Sita",
        "age": 21,
        "course": "Java"
    },
    103: {
        "name": "Hari",
        "age": 19,
        "course": "Python"
    }
}

# 1. Display all students
print("All students:")
for student_id, details in students.items():
    print(student_id, details)

# 2. Display details of student 102
print("\nDetails of student 102:")
print(students[102])

# 3. Change student 103's course
students[103]["course"] = "Data Science"

# 4. Add a new student with ID 104
students[104] = {
    "name": "Gita",
    "age": 22,
    "course": "C++"
}

# 5. Remove student 101
del students[101]

# 6. Display the final dictionary
print("\nFinal dictionary:")
print(students)


# Challenge: Ask the user for a student ID
student_id = int(input("\nEnter a student ID: "))

if student_id in students:
    print("Student information:", students[student_id])
else:
    print("Student ID does not exist.")