
import random
from string import ascii_lowercase
from string import ascii_uppercase
from string import punctuation
num_list = ['0','1','2','3','4','5','6','7','8','9']

def create_password():

    lower_case = int(input('The number of lowercase letters the password will contain: '))
    upper_case = int(input('The number of uppercase letters the password will contain: '))
    special_characters = int(input('The number of special characters the password will contain: '))
    number = int(input('The number of numbers the password will contain: '))

    random_lower_case = random.sample(ascii_lowercase, lower_case)
    random_upper_case = random.sample(ascii_uppercase, upper_case)
    random_special_characters = random.sample(punctuation, special_characters)
    random_number = random.sample(num_list, number)

    password = random_lower_case + random_upper_case + random_special_characters + random_number
    random.shuffle(password)
    password = ''.join(password)

    print(f'Your password is: {password}')

create_password()