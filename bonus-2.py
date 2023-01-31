list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#even_list = sorted( lambda x: x %2 != 0)

even_list =  list( filter(lambda x: x%2 == 0, list_numbers) )
print("even numbers are: ", even_list)


odd_list = list( filter(lambda x:x %2 != 0, list_numbers) )
print("odd numbers are: ", odd_list)


