#  Answer 4
"""Create a user interface that generates a random password with the given 
user input such as length, number of lowercase letters and uppercase letters and 
adding special characters(!,?, .,etc.)"""

from tkinter import *
import random
import string


screen = Tk()

screen.title("Password Generator!")
screen.geometry('350x200')
screen.title("Password Generator!")

length_text = Label(screen, text="Enter the number of characters")
length_text.pack()

length = Entry(screen, width=20)
length.pack(padx=20, pady=20)

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num =string.digits
speialchar = string.punctuation
all = lower + upper + num + speialchar
def generate():
    l = int(length.get())
    temp = random.sample(all,l)
    password= Label(screen)
    password.configure(text ="Password: "+ "".join(temp))
    password.pack()
generate_btn = Button(screen, text="Generate Password", command=generate)
generate_btn.pack()

screen.mainloop()

