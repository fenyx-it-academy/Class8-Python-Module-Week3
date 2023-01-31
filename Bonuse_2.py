my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x: (x % 2 == 0), my_list))
odd_list = list(filter(lambda x: (x % 2 != 0), my_list))
print('Even numbers from the said list: ', even_list)
print('Odd numbers from the said list: ', odd_list)
