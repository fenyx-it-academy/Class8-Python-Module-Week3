
lenght=int(input("enter lenght: "))
lowerNumber=int(input("enter number lowercase latter: "))
upperNumber=int(input("enter number of uppercase Latter: "))
special=input("enter spacial charackters like: !,?, .,etc. : ")


# lenghtNumber=10
# lowerNumber=3
# upperNumber=4
# special="!,?"

lowerLatters='abcdefghijklmnopqrstuvwxyz'
upperLatters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"


import random

def pickRandom(chars,number):
    result=[]
    for i in range( number):
        result.append(random.choice(chars))
    return result
        
lower=pickRandom(lowerLatters, lowerNumber)
upper=pickRandom(upperLatters, upperNumber)

#making list of spacial charackter
special=special.split(",")

#Generate reamaining numbers
digitNumber=lenght-(lowerNumber+upperNumber+len(special))
number=pickRandom(numbers, digitNumber)



password=number+lower+upper+special
random.shuffle(password)
password = ''.join([str(elem) for elem in password])

print(password)



