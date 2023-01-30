import random
from tkinter import *


def generate():
    
    password = gen_pass(password_length.get(), lowercase_len.get(), uppercase_len.get(),special_char.get())
    if password == 1:
       password_lable.config(text='Total number of inputs are more than password length, please try again',fg='red', font=('Arial', 9))
    elif password == 2:
        password_lable.config( text='Total number of inputs are less than password length, please try again', fg='red', font=('Arial', 9))
    else:
       password_lable.config(text=f'Password is: {password}', fg='black', font=('Arial', 12))
    
    
     
    

def gen_pass(pl,lc,uc,sc):
    password_length = int(pl)
    lowercase_len = int(lc)
    uppercase_len = int(uc)
    special_char = sc
    lowercase_alpha = "abcdefghijklmnopqrstuvwxyz"
    uppercase_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password=""
    if (lowercase_len+uppercase_len+len(special_char)) > password_length:
       return 1
    elif (lowercase_len+uppercase_len+len(special_char)) < password_length:
       return 2
    else:
        lower = random.choices(lowercase_alpha, k=lowercase_len)
        upper = random.choices(uppercase_alpha, k=uppercase_len)
        lower.extend(upper)
        lower.extend(special_char)
        random.shuffle(lower)
        print(lower)
        for i in lower:
             password+=i
    return password 

screen = Tk()
title = screen.title('Random Password Generator')
canvas = Canvas(screen, width=400,height=500)
canvas.pack()

password_length = Entry(screen, text='', font=('Arial', 12))
password_length_label = Label(screen, text='Enter Password Length: ', font=('Arial', 12))
canvas.create_window(200, 40, window=password_length_label)
canvas.create_window(200, 70, window=password_length)

lowercase_len = Entry(screen, text='', font=('Arial', 12))
lowercase_len_label = Label(screen, text='Enter number of lowercase letters: ', font=('Arial', 12))
canvas.create_window(200, 120, window=lowercase_len_label)
canvas.create_window(200, 150, window=lowercase_len)

uppercase_len = Entry(screen, text='', font=('Arial', 12))
uppercase_len_label = Label(screen, text='Enter number of uppercase letters: ', font=('Arial', 12))
canvas.create_window(200, 200, window=uppercase_len_label)
canvas.create_window(200, 230, window=uppercase_len)

special_char = Entry(screen, text='', font=('Arial', 12))
special_char_label = Label(screen, text='Enter any special characters: ', font=('Arial', 12))
canvas.create_window(200, 280, window=special_char_label)
canvas.create_window(200, 300, window=special_char)


btn = Button(screen, text='Generate', font=('Arial', 15), bg='green', fg='#fff', command=generate)
canvas.create_window(200, 360, window=btn)
password_lable = Label(screen, text='')
canvas.create_window(200, 400, window=password_lable)

screen.mainloop()





