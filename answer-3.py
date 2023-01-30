
def is_perfect_number(number):
    ''' A function to check if a number is a perfect number.
    
    Returns True or False. '''
    
    # If the number is negative or 0, return False.
    if number <= 0:
        return False

    # Calculating the divisors of the number.
    divisors = [1]
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)

    # Calculating the sum of the divisors and checking if the number is equal to the sum of its divisors.
    sum_of_divisors = sum(divisors)
    if number == sum_of_divisors:
        return True
    else:
        return False
        

number = int(input("Enter a number to check if it's a perect number: "))

if is_perfect_number(number):
    print (f"Number {number} is a perfect number")
else:
    print (f"Number {number} is not a perfect number")