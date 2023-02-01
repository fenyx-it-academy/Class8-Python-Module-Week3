"""
Edited from codes I found on the internet.
"""

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda x: x % 2 == 0, mylist))

odd = list(filter(lambda x: x % 2 != 0, mylist))

print("Even numbers:", even)

print("Odd numbers:", odd)