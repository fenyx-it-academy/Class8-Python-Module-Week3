import random
import string

def generate_password(length, num_lowercase, num_uppercase, num_special_chars):
    password = ''
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    special_chars = '!@#$%^&*()_+-=[]{}'
    
    for i in range(num_lowercase):
        password += random.choice(lowercase_chars)
    for i in range(num_uppercase):
        password += random.choice(uppercase_chars)
    for i in range(num_special_chars):
        password += random.choice(special_chars)
        
    while len(password) < length:
        password += random.choice(lowercase_chars + uppercase_chars + special_chars)
        
    password = ''.join(random.sample(password, len(password)))
    return password
