def check_perfect(n):
    """
    This function checks if the given number
    is a perfect number or not
    """
    temp = 0
    for i in range(1,n+1):
        temp += i
        if (n/i)% 2 == 0 and temp == n:  # check if n is perfect number
            print('Perfect number')
            break
    else:
        print('Not a perfect number ')



check_perfect(6)