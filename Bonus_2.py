# Bonus 2 Answer
# Write a Python program to filter a list of integers using Lambda.

# Original list of integers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers from the said list: [2, 4, 6, 8, 10]

# Odd numbers from the said list: [1, 3, 5, 7, 9]

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(number)

print("Even numbers from the said list:")
even_nums = list(filter(lambda x: x%2 == 0, number))
print(even_nums)

print("Odd numbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, number))
print(odd_nums)