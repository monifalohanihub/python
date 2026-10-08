marks = [75, 82, 68, 90, 55, 88, 72, 95]

# 1. Print all marks
print("All marks:", marks)

# 2. Calculate total marks
total = sum(marks)
print("Total marks:", total)

# 3. Calculate average marks
average = total / len(marks)
print("Average marks:", average)

# 4. Find highest mark
highest = max(marks)
print("Highest mark:", highest)

# 5. Find lowest mark
lowest = min(marks)
print("Lowest mark:", lowest)

# 6. Count students who scored 75 or more
count = 0

for mark in marks:
    if mark >= 75:
        count += 1

print("Students scoring 75 or more:", count)

# 7. Sort marks from highest to lowest
marks.sort(reverse=True)
print("Marks from highest to lowest:", marks)


# Challenge: Add another student's mark
new_mark = int(input("Enter another student's mark: "))
marks.append(new_mark)

print("\nUpdated marks:", marks)
print("Updated total:", sum(marks))
print("Updated average:", sum(marks) / len(marks))
print("Updated highest mark:", max(marks))
print("Updated lowest mark:", min(marks))

count = 0
for mark in marks:
    if mark >= 75:
        count += 1

print("Updated students scoring 75 or more:", count)

marks.sort(reverse=True)
print("Updated marks from highest to lowest:", marks)