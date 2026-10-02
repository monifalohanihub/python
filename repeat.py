text = input("Enter a string: ")

for char in text:
    if text.count(char) > 1:
        print("First repeated character:", char)
        break