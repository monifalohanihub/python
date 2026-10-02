password = ""

while password != "python123":
    password = input("Enter password: ")

    if password == "python123":
        print("Correct password!")
    else:
        print("Invalid password!")