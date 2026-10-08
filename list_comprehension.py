list = [1, 2, 3, 4, 5]
b = (num for num in list if num % 2 == 1)
print(b)
print(next(b))
print(next(b))
print(next(b))
