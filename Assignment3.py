# # Assignment 3
''' this function is used to check whether a number is perfect or not '''
def perf_num(n):
  sum = 0
  for i in range(1, n):              # the number n is not included
    if(n % i == 0):
        sum += i
  return sum == n

# asking to give a number to check
n = int(input("Please enter a number: "))
if perf_num(n):
    print(f" {n} is a perfect number!")
else:
    print(f" {n} is not a perfect number!")