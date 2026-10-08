marks = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 65,
    "Gita": 92,
    "John": 55
}

# 1. Print all students and marks
for student, mark in marks.items():
    print(student, ":", mark)

# 2. Find the total marks
total = sum(marks.values())
print("Total marks:", total)

# 3. Find the average marks
average = total / len(marks)
print("Average marks:", average)

# 4. Find the highest mark
highest = max(marks.values())
print("Highest mark:", highest)

# 5. Find the lowest mark
lowest = min(marks.values())
print("Lowest mark:", lowest)

# 6. Find the student with the highest mark
top_student = max(marks, key=marks.get)
print("Student with highest mark:", top_student)