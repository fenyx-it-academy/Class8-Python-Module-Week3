import random
import string
import tkinter as tk

def generate_password():
    length = int(length_entry.get())
    num_lower = int(lower_entry.get())
    num_upper = int(upper_entry.get())
    num_special = int(special_entry.get())
    num_digits = length - num_lower - num_upper - num_special
    if num_digits == 0:
     password = ''.join(random.choices(string. ascii_lowercase, k=num_lower))
     password += ''.join(random.choices(string. ascii_uppercase, k=num_upper))
     password += ''.join(random.choices(string. punctuation, k=num_special))
     password = ''.join(random.sample( password, len(password)))
     password_label.config(text= password)
    else:
        password = "Error! No.of characters doesn't match length"
        password_label.config(text= password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password length")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

lower_label = tk.Label(root, text="Number of lowercase letters")
lower_label.grid(row=1, column=0)
lower_entry = tk.Entry(root)
lower_entry.grid(row=1, column=1)

upper_label = tk.Label(root, text="Number of uppercase letters")
upper_label.grid(row=2, column=0)
upper_entry = tk.Entry(root)
upper_entry.grid(row=2, column=1)

special_label = tk.Label(root, text="Number of special characters")
special_label.grid(row=3, column=0)
special_entry = tk.Entry(root)
special_entry.grid(row=3, column=1)

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

password_label = tk.Label(root, text="")
password_label.grid(row=5, column=0, columnspan=2)


root.mainloop() 