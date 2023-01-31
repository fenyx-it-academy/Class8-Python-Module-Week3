def pascal_function(n):
 for i in range(0, n+1):
    first = 1
    for j in range(1, i+1):
        print('', first, end=' ')#make first number always 1
        first = first * (i - j) 
        first //= j
        # print("first is:" , first)
    print("")

n= int(input("Enter number of rows:"))
pascal_function(n)