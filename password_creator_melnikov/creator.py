import tkinter as tk
import passfunc as pf
from tkinter import messagebox

def getint(x):
    return int(x.get())

def clicked():
    messagebox.showinfo(
        message=f'''There is your safe password \n \
            {pf.generate_password(getint(length_p), numlet=getint(number_let), char=chk_char.get())} \n \
            Copy it in the safe place.''')

screen = tk.Tk()
title = screen.title('Password Creator')
screen.geometry('400x270')


#label
label = tk.Label(screen, text='The password will contain uppercase \n and lowercase Latin letters as well \n as numbers and symbols.', font=('Roboto', 14))
label.pack(padx=20, pady=30)


#greed with inputs, labelframe
labelframe = tk.Frame(screen)
labelframe.columnconfigure(0, weight=1)
labelframe.columnconfigure(1, weight=1)

label1 = tk.Label(labelframe, text='Password Legnth', font=("Roboto", 12))
label1.grid(row=0, column=0, sticky=tk.W+tk.E)

length_p = tk.Entry(labelframe, font=('Roboto', 12), width=10)
length_p.grid(row=0, column=1, sticky=tk.W+tk.E)

label2 = tk.Label(labelframe, text='Number of letters', font=('Roboto', 12))
label2.grid(row=1, column=0, sticky=tk.W+tk.E)

number_let = tk.Entry(labelframe, font=('Roboto', 12), width=10)
number_let.grid(row=1, column=1, sticky=tk.W+tk.E)

chk_char = tk.BooleanVar()
chk_char.set(True)
ischaruse = tk.Checkbutton(labelframe, text='Use special characters', var=chk_char)
ischaruse.grid(row=2, column=1)
labelframe.pack()

#button frame
buttonframe = tk.Frame(screen)

submit_button = tk.Button(buttonframe, text='Submit', font=('Roboto', 14), command=clicked)
submit_button.config(height= 20, width=26)
submit_button.pack(pady=20)

buttonframe.pack()

screen.mainloop()