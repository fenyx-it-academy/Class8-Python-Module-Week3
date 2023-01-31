##  Assignment 3
from functools import reduce
def divisors(number):
    """this function , to test if the number is perfect on not"""
    global list1
    counter1 = 1
    list1 = []
    while counter1 < number : 
        if number % counter1 == 0 :
            list1.append(counter1) 
        counter1 +=1

    sum_numbers = reduce(lambda a,b : a+b , list1)
    if sum_numbers == number : 
        print("its a perfect number ", number )
        print("his divisors is : ", list1)

    else : 
        print("its not a perfect number ", number )
        print("his divisors is : ", list1)

number = int(input("please enter the number : "))
divisors(number)
