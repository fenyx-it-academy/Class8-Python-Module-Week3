
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list(filter(lambda x: x % 2 == 0, list1))
odd_list = list(filter(lambda x: x % 2 != 0, list1))

print(even_list)
print(odd_list)
 