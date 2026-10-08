employee = {
    "name": "John",
    "age": 30,
    "department": "IT",
    "salary": 50000,
    "city": "Kathmandu"
}

# 1. Remove the age key
del employee["age"]

# 2. Remove the city key
employee.pop("city")

# 3. Print the dictionary
print(employee)

# 4. Safely try to remove the email key
employee.pop("email", None)

print(employee)