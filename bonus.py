#  Bonus 2
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
even_list = list(filter(lambda x: (x%2 == 0) , my_list)) # using lambda to filter even numbers
print("the even numbers in the list are: ")
print(even_list)
odd_list = list(filter(lambda x: (x%2 != 0) , my_list)) # using lambda to filter odd numbers
print("the odd numbers in the list are: ")
print(odd_list)