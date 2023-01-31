## Assignment 1

def Pascals_triangle( n ) :
    """this function ,creat the pascals triangle """
    res = [[1]]
    y = []
    head = [1]
    print(head)
    for i in range(0,n - 1):
        y = [0] + res[-1] + [0] 
        row = []
        for m in range(len(res) + 1) :
            row.append(y[m] + y[m + 1])
        res.append(row)
        print(row)
      
n = int(input("please write the number of rows "))
Pascals_triangle(n)