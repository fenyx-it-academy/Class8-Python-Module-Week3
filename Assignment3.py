def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        print(f"{n} is a perfect number")
        return True
    else:
        print(f"{n} is NOT a perfect number")
        return False
    
