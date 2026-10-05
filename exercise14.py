book = {
    "title": "Python Basics",
    "author": "John Smith",
    "year": 2025,
    "price": 500
}

# 1. Print all keys
print(book.keys())

# 2. Print all values
print(book.values())

# 3. Print all key-value pairs
print(book.items())

# Display each key and value using a for loop
for key, value in book.items():
    print(key, "=", value)