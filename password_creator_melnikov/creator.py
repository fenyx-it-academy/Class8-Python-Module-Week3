import tkinter as tk
import passfunc as pf
from tkinter import messagebox

def clicked():
    messagebox.showinfo(message=f'There is your safe password \n {pf.generate_password(length_p.get())} \n Copy it in the safe place.')

screen = tk.Tk()
title = screen.title('Password Creator')
screen.geometry('400x230')
# canvas = tk.Canvas(screen, width=300, height=500)
# canvas.pack()


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


# label2 = tk.Label(labelframe, text='Password count', font=('Roboto', 12))
# label2.grid(row=1, column=0, sticky=tk.W+tk.E)

# count = tk.Entry(labelframe, font=('Roboto', 12), width=10)
# count.grid(row=1, column=1, sticky=tk.W+tk.E)

labelframe.pack()

#button frame
buttonframe = tk.Frame(screen)
submit_button = tk.Button(buttonframe, text='Submit', font=('Roboto', 14), command=clicked)
submit_button.pack(fill='x', pady=20)
buttonframe.pack()

screen.mainloop()