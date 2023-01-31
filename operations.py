def add(a, b):
     """This program adds two
    numbers and return the result"""

     result = a + b
     return result

def subtract(a, b):
     """This program adds two
    numbers and return the result"""

     result = a - b
     return result

def multiply(a, b):
     """This program adds two
     numbers and return the result"""

     result = a * b
     return result

def divide(a, b):
     """This program adds two
    
     numbers and return the result"""

     result = a / b
     return result

def power(a, b):
     """This program adds two
     numbers and return the result"""
     result = a ** b
     return result

def modulo(a, b):
     """This program adds two
    numbers and return the result"""


     result = a % b
     return result

def sqroot(a):

     result = a ** 0.5
     return result

     result = a ** b
     return result

#recurrsion
def factorial(n):
  if n<=1:           #stop machanizim
    return 1
  else:
    return n*factorial(n-1)          #factorial
#factorical (4)
#4*factorical(3)
#4*3*factorial(2)
#4*3*2*factorial(1)
#4*3*2*1


def fib(n):
  if n<=2:         #stop machanisim
    return 1
  else :
    return fib(n-1)+fib(n-2)       #fiboncai function

fib(10)

#it is also possible to define a  function

PI = 3.1415926535897932