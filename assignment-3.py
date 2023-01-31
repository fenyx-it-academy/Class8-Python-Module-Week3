
def is_perfect(n):

    total = 0

    for x in range (1,n):
       if n % x == 0 : 
        total += x

    if total == n :
         return("Yes")
    else:
         return("No")


number = input("enter number: ")
number = int (number)

print ("is the number perfect: ", end="")
print(is_perfect(number))