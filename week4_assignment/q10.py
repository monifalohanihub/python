# 10. Simple Inventory

inventory = {
    "apple": 20,
    "banana": 15,
    "mango": 10,
    "orange": 8
}

item = input("Enter an item name: ").lower()

if item in inventory:
    sold = int(input("Enter quantity sold: "))

    if sold <= inventory[item]:
        inventory[item] -= sold

        if inventory[item] == 0:
            del inventory[item]

        print("Updated inventory:", inventory)
    else:
        print("Not enough stock available.")
else:
    print("Item does not exist in inventory.")