import random as rnd
from string import punctuation

# size variables of each character groups and total length
pass_lenght = int(input('\nPasword length: '))
nlower = int(input('Number of Lowercase characters: '))
nUpper = int(input('Number of Uppercase characters: '))
nspec_chars = int(input('Number of special characters: '))
nint = pass_lenght - nlower - nUpper - nspec_chars
#
pchar_list=[]

def pick_lowercase(l):
    # function returns required amount of lowercase letter characters
    lower_chars = list(map(chr, range(97, 123)))
    return [rnd.choice(lower_chars) for i in range(l)]

def pick_uppercase(u):
    # function returns required amount of uppercase letter characters
    upper_chars = list(map(chr, range(65, 91)))
    return [rnd.choice(upper_chars) for i in range(u)]

def spec_chars(s):
    # function returns required amount of special characters
    spec_chars = list(set(punctuation))
    return [rnd.choice(spec_chars) for i in range(s)]

int_chars = [str(rnd.randint(0, 9)) for i in range(nint)]


pchar_list = pick_lowercase(nlower) + pick_uppercase(nUpper) + spec_chars(nspec_chars) + int_chars
rnd.shuffle(pchar_list)

password = ''.join(pchar_list)
print(f"\nPassword: {password}\n")
