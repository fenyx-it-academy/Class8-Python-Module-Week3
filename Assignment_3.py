def perfect_num_checker(n):
    sum=0
    for i in range(1,n+1):
        if n % i == 0:
            sum+=i
    sum=sum//2
    if n == sum:
       print(n, " is a perfet number")
    else:
        print(n, " is not a perfer number")

n = int(input("Enter a number:"))
perfect_num_checker(n)