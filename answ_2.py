## Assignment 2

# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow


my_str=input('Insert a hyphen-separated sequence of words,please!')
my_list=my_str.split ("-") #making a list
my_list_sort=sorted(my_list) #making sorted list
my_str_sort='-'.join(my_list_sort) #making sorted string
print("After sorting alphabetically it is look like so:", my_str_sort) #output result