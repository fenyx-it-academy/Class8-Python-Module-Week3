import random
import secrets
import string

#password_length = 10
#number_lowercase = 4
#number_uppercase = 4
#number_digits = 5
#number_special_characters = 3


print ("Welcome to password generator!")
print ("How would you like your new password...")
password_length = int (input("enter password length: "))
number_lowercase = int (input("how many lowercase characters: "))
number_uppercase = int (input("how many uppercase characters: "))
number_digits = int (input("how many digits: "))
number_special_characters = int (input("how many special characters: "))



def generate_password (password_length, number_lowercase,number_uppercase, number_digits, number_special_characters) :

    letter_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    #rand_lower = ""
    #rand_upper = ""
    #rand_digit = ""
    #rand_special = ""
    password_char_list = ""

    for x in range(1, number_lowercase) :
        password_char_list += random.choice(letter_lower)


    for x in range(1, number_uppercase) :
        password_char_list += random.choice(letters_upper)

    for x in range(1, number_digits) :
        password_char_list += random.choice(digits)

        
    for x in range(1, number_special_characters) :
        password_char_list += random.choice(special_chars)




    #print (password_char_list)


    final_password = []
    for x in range(password_length):
    
        random_char = random.choice(password_char_list)
        final_password.append(random_char)
    


    final_password = "".join(final_password)

    print(final_password)


print ("your new password is: ", end="")
generate_password (password_length, number_lowercase,number_uppercase, number_digits, number_special_characters) 
