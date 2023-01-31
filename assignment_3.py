
def perfectnumber(n):
    for i in range(1,n):
        sum1=0
        if n % i==0:
            sum1 += i
    if sum1==n:
        print(f'{n} is a perfect number')
    else:
        print(f'{n} is not a perfect number')


perfectnumber(14)