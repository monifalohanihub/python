product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 75000,
    "quantity": 5
}

# 1. Display product name and brand
print("Product name:", product["name"])
print("Brand:", product["brand"])

# 2. Display the price
print("Price:", product["price"])

# 3. Display the available quantity
print("Available quantity:", product["quantity"])

# 4. Calculate the total value
total_value = product["price"] * product["quantity"]
print("Total value:", total_value)

# Update quantity after selling 2 laptops
product["quantity"] = product["quantity"] - 2

print("Updated quantity:", product["quantity"])