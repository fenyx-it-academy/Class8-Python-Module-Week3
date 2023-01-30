# ## Assignment 3
# Write a Python function to check whether a number is perfect or not.
# According to [Wikipedia](https://en.wikipedia.org/wiki/Perfect_number) : 
# In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, 
# that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). 
# Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
# Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

def perfect_number(number):
    '''Check if the integer number is perfect and returns bolean'''
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return ('NOT PERFECT', 'PERFECT')[sum == number]

#call the function with integer input
num = int(input('Number  '))
print(perfect_number(num))