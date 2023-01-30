# ## Assignment 4

# Create a user interface that generates a random password with the given user input such as length, 
# number of lowercase letters and uppercase letters and adding special characters(!,?, .,etc.)


import random as ran
import string as st


def generate_password(length):
    '''Returns a password consisting of lowercase and uppercase English letters, 
    numbers and symbols, except for those easily confused with each other'''

    length = int(length)
    digits = [digit for digit in st.digits if digit not in '0']
    letters = [letter for letter in st.ascii_letters if letter not in 'lIoO']
    characters = [char for char in st.punctuation]
    
    password = ran.sample(letters, int(length - 3)) + ran.sample(digits, 2) + ran.sample(characters, 1)
    ran.shuffle(password)
    return "".join(password)
    

def generate_passwords(count, length):
    passwords = [generate_password(int(length)) for _ in range(int(count))]
    return passwords
    
