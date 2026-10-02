items = ["red", "blue", "green", "red", "yellow"]

for i in range(len(items)):
    if items[i] in items[:i]:
        print("Duplicate found:", items[i])
        break