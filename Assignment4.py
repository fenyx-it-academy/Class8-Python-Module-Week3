# # Assignment 4
''' this program composes a random password '''
import random
import string

def random_password(length):
    items = string.ascii_letters + string.digits + string.punctuation # upper & lowercase letters , numbers and special symbols
    password = ''.join(random.choice(items) for i in range(length))     # generating the password from the random choices
    print("here is your random password :", password)
# # examples
random_password(8)
random_password(10)
