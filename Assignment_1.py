# Answer 1
# Write a Python function that prints out the first n rows of Pascal's triangle. Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

# Sample Pascal's triangle :


from math import factorial
def number_of_rows(n):
    for i in range(n):
        for j in range(n - i + 1):
            print(end=" ")
        for j in range(i + 1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print("")
n = 5 
number_of_rows(n)