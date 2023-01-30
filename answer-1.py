
row_number = 0

def print_pascal_triangle(n):
    ''' A recursive function to print the first n rows of Pascal triangle.
    
    Returns the the nth row as a list of integers. '''
    
    # initialize the first row as a list of 1s of size n.
    row = [1] * n
    
    # The base condition of the recursion, when n is 1.
    if n == 0:
        return [1]
    else:
        previous_row = print_pascal_triangle(n - 1)
        
        # calculate the row valuse except the first and last values as they are always 1.
        for i in range(1, n - 1):
            row[i] = previous_row[i-1] + previous_row[i]
            
        # print the current row.
        print(" " * (row_number - n), end="")
        print(row)
        return row

row_number = int(input('Enter the numbers of rows from Pascal triangle you want to print: '))
print_pascal_triangle(row_number)
