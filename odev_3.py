def perfect_number(n):
     
    
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")
    
n = int(input("Enter any number: "))

perfect_number(n)