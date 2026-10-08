# 7. Common Elements

list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 50, 70, 80, 90]

common = set(list1) & set(list2)
only_list1 = set(list1) - set(list2)
only_list2 = set(list2) - set(list1)

print("Present in both lists:", sorted(common))
print("Only in list1:", sorted(only_list1))
print("Only in list2:", sorted(only_list2))