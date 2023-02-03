

def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0 :
            sum += i
    if sum == num:
        print(f'{num} is a perfect number')
    else:
        print(f"{num} isn't a perfect number")

perfect_number(6)