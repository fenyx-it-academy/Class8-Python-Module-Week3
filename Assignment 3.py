def is_perfect(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    sum_of_divisors = sum(divisors)
    if sum_of_divisors == num:
        return True
    else:
        return False
