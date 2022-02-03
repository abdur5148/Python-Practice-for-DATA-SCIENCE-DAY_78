list1 = [12, 24, 35, 70, 88, 120, 155]
list1 = [x for (i, x) in enumerate(list1) if i % 2 != 0 and i <= 6]
print(list1)
