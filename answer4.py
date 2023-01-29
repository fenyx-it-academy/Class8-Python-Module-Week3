from tkinter import *
from tkinter import filedialog
import random
import string

def generate_passowrd():
    """
    This function is used to generate random password
    and display the password in tkinter screen
    """
    try:
        global user_entry
        pass_len = int(user_entry.get())         # get password length from user
        rand_num = random.randrange(0, 10)     # random number from 0 to 9
        lower_case = string.ascii_lowercase    # random upper case letter
        upper_case = string.ascii_uppercase    # random upper case letter 
        special_char = string.punctuation      # random special character
        rand_pass = ''.join([lower_case,upper_case,special_char,str(rand_num)])  
        rand_pass = random.sample(rand_pass,pass_len)   # generate the random password
        password_label.config(text=rand_pass)
    except ValueError:
        password_label.config(text='ERROR: Please Enter a number')
        


   
# start screen
screen = Tk()
title = screen.title('Password generator')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# declare labels and buttons
greeting_label = Label(screen, text='WELCOME TO PASSWORD GENERATOR ', font=('Times', 15))
user_entry = Entry(screen, text='password length', font=('Arial', 15))
username_label = Label(screen, text='Enter your password length: ', font=('Calibri', 15))
password_label = Label(screen, text= "", font=('Arial', 15))
btn = Button(screen, bg='dark blue', padx='22', pady='5', font=('Arial', 15)
             , fg='light blue', text='Generate password',command= generate_passowrd)


# Place to the canvas
canvas.create_window(250, 100, window=greeting_label)
canvas.create_window(250, 170, window=username_label)
canvas.create_window(250, 220, window=user_entry)
canvas.create_window(250, 280, window=btn)
canvas.create_window(250, 325, window=password_label)


screen.mainloop()



    
