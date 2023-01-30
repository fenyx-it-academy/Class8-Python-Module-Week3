# ## Assignment 1

# Write a Python function that prints out the first n rows of Pascal's triangle.
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
# Sample Pascal's triangle :
# ![pascal-traingle](https://user-images.githubusercontent.com/45574672/215293769-36573e97-fb93-4ed9-8574-17db7ee04cb7.png)
# Pascal's triangle
# Each number is the two numbers above it added together

def pascal_triangle(s):
    '''Returns n's row in Pascal's triangle
    Print included function'''

    #create triangle as nested list of numbers
    l, triangle = [1], [[1]]
    for _ in range(s):
        l = [a + b for a, b in zip([*l, 0], [0, *l])]
        triangle.append(l)

    # define base of triangle
    basis = len(' '.join(map(str, triangle[-1])))
    for i in triangle:
        print(' '.join(map(str, i)).center(basis))
        # print(.center(basis))

#call the function 
n = int(input('How many rows? ')) - 1
pascal_triangle(n)


