## Assignment 3

#Write a Python function to check whether a number is perfect or not.


def perf_check(num):
    """function to check whether a number is perfect or not"""
    sum_d=0
    for i in range (1,num):
       if num%i==0: 
        sum_d +=i
    if sum_d==num:
         return("Perfect")
    else:
         return("Not perfect")


num=int(input(("Insert a number - ")))#call the function with integer input
print(perf_check(num))