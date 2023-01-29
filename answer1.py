from math import factorial


def pascal_triangel(n):    
    """
    This function prints out
    the first n rows of Pascal's triangle
    """
    for i in range(n):
        for j in range(n-i+1):
            print(end=' ') # left space
    
        for j in range(i+1):
            
            # nCr = n!/((n-r)!*r!)
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
            
        print()
    


pascal_triangel(5)