# 1. Username Generator

name = input("Enter your full name: ")
username = "_".join(name.split()).lower()
print(username)