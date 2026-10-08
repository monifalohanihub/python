name = input("Enter a name: ")
vowels = "aeiou"
found_vowels = [letter for letter in name if letter.lower() in vowels]

print("Vowels found in the name:", found_vowels)
