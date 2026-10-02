number = input("Enter the numbers: ").split()
total = 0
for i in number:
    i = int(i)
    if i % 2 != 0:
        total += i
print(total)
