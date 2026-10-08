# 4. Sentence Analysis

sentence = input("Enter a sentence: ")

sentence = " ".join(sentence.split()).lower()
words = sentence.split()

print("Cleaned sentence:", sentence)
print("Total number of words:", len(words))
print("Python appears:", words.count("python"), "time(s)")

if words:
    print("Longest word:", max(words, key=len))