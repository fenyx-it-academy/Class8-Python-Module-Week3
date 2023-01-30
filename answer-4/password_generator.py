
import random

SPECIAL_CHARS = """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
NUMBERS = "0123456789"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"


def Generate_random_password(number_of_lower_case_letters = 0, number_of_upper_case_letters = 0, number_of_numbers = 0, number_of_special_chars = 0):
    """ A function to generate a random password.
    
    Accepts the number of upper-case letters, lower-casw letters, digits and special characters.
    
    Returns the password as a string."""
    
    # Initialize a list to store the password characters.
    password_elements = []    
    
    # Adding the password characters to the list.
    for i in range(number_of_lower_case_letters):
        password_elements.append(random.choice(LOWER_LETTERS))
    for i in range(number_of_upper_case_letters):
        password_elements.append(random.choice(UPPER_LETTERS))
    for i in range(number_of_numbers):
        password_elements.append(random.choice(NUMBERS))
    for i in range(number_of_special_chars):
        password_elements.append(random.choice(SPECIAL_CHARS))
    
    # Shuffle the elements of the list.
    random.shuffle(password_elements)
    
    # Convert the list to a string and return the final password string.
    password = ''.join(password_elements)
    return password

    