### Bonus 2

# Write a Python program to filter a list of integers using Lambda.

# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers from the said list:
# [2, 4, 6, 8, 10]

# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list(filter(lambda x: (x%2 == 0) , my_list))# Even numbers from the list

print(even_list)

odd_list= list(filter(lambda x: (x%2 == 1), my_list)) # Odd numbers from the list

print(odd_list)