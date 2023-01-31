def is_perfect_number(number):
    """ a function that accepts an integer and return True
     if the number is a perfect number or False if not"""
    sum_1 = 0
    for i in range(1, number):
        if number % i == 0:
            sum_1 += i
    sum_2 = (sum_1 + number) / 2    
    return sum_1 == number and sum_2 == number

number = input('enter a positive enteger \n')
try:
    number = int(number)
except:
    print("Invalid input, please enter an integer")
    quit()
if is_perfect_number(number):
    print (f"The number {number} is a perfect number")
else:
    print (f"The number {number} is not a perfect number")
     