numbers = [45, 12, 78, 3, 56, 23, 89, 10]

# 1. Print the original list
print("Original list:", numbers)

# 2. Sort the list in ascending order
numbers.sort()
print("Ascending order:", numbers)

# 3. Sort the list in descending order
numbers.sort(reverse=True)
print("Descending order:", numbers)

# 4. Find the smallest number
print("Smallest number:", min(numbers))

# 5. Find the largest number
print("Largest number:", max(numbers))


# List of five names
names = ["Ram", "Sita", "Hari", "Gita", "John"]

# Sort names alphabetically using sorted()
sorted_names = sorted(names)

print("Original names:", names)
print("Alphabetical order:", sorted_names)