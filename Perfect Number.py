def isPerfect(n):
    if sum([i for i in range(1,n) if n % i == 0]) == n:
        return True

n = int(input('Number to be checked if it is perfect: '))
if isPerfect(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")    



