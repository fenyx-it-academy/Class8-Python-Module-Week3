lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x : x % 2 == 0, lst ))
odd_numbers = list(filter(lambda x : x % 2 != 0, lst))
print(even_numbers)
print(odd_numbers)