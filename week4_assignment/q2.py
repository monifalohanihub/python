# 2. Student Marks Analysis

marks = [45, 78, 62, 89, 55, 92, 38, 76]

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)
above_average = sum(1 for mark in marks if mark > average)

print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Average mark:", average)
print("Students above average:", above_average)
print("Ascending order:", sorted(marks))