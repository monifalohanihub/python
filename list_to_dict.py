days = [0, 1, 2, 3, 4, 5, 6]
temperature = [32, 45, 50, 60, 70, 80, 90]

dict_days = { }
for i in range(len(days)):
    dict_days[days[i]] = temperature[i]
print(dict_days)