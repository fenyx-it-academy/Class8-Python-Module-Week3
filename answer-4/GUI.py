
import password_generator
import tkinter as tk
import os

current_path = os.path.dirname(os.path.realpath(__file__))

def generate_btn_handler():
    """ A function to handle the press event of the generate button """
    
    # Getting the values entered by the user
    lower_case_letters = int(lower_case_entry.get())
    upper_case_letters = int(upper_case_entry.get())
    numbers = int(numbers_entry.get())
    special_chars = int(special_chars_entry.get())
    
    # Creating the password from the values entered by the user using the password_generator module from password_generator.py
    password = password_generator.Generate_random_password(lower_case_letters, upper_case_letters, numbers, special_chars)
    
    # Clearing the password field and displaying the generated password
    password_field.config(state="normal")
    password_field.delete(0, tk.END)
    password_field.insert(0, password)
    password_field.config(state="readonly")
    

# Creating the main window
screen = tk.Tk()
screen.title("Password Generator")
canvas = tk.Canvas(screen, width=500, height=450)
canvas.pack()

# Displaying the logo image
logo = tk.PhotoImage(file = current_path + "\psw.png")
logo = logo.subsample(3, 3)
canvas.create_image(250, 90, image = logo)
canvas.create_text(250, 200, text = "How would you like your password?", font=("Arial", 17, "bold"), fill= "#556080")

canvas.create_text(250, 250, text = "Lower-case Letters: ", font = ("Arial", 11, "bold"), anchor="e", fill= "#556080")
canvas.create_text(250, 270, text = "Upper-case Letters: ", font = ("Arial", 11, "bold"), anchor="e", fill= "#556080")
canvas.create_text(250, 290, text = "Numbers: ", font = ("Arial", 11, "bold"), anchor="e", fill= "#556080")
canvas.create_text(250, 310, text = "Special Characters: ", font = ("Arial", 11, "bold"), anchor="e", fill= "#556080")

# Entry boxes for the password generation options with default values of 3
lower_case_entry, upper_case_entry, numbers_entry, special_chars_entry  = tk.Entry(screen), tk.Entry(screen), tk.Entry(screen), tk.Entry(screen)
lower_case_entry.insert(0, 3)
canvas.create_window(250, 250, window = lower_case_entry, anchor="w")
upper_case_entry.insert(0, 3)
canvas.create_window(250, 270, window = upper_case_entry, anchor="w")
numbers_entry.insert(0, 3)
canvas.create_window(250, 290, window = numbers_entry, anchor="w")
special_chars_entry.insert(0, 3)
canvas.create_window(250, 310, window = special_chars_entry, anchor="w")

# Create the generate button handler function and assignment to it to gen
generate_btn = tk.Button(screen, text = "Generate Password", command = generate_btn_handler, relief="groove")
generate_btn.config(fg="#556080", font=("Arial", 15))
canvas.create_window(250, 350, window = generate_btn)

# creating the password field to display the generated password
password_field = tk.Entry(screen, font=("Arial", 20, "bold"), fg="#e4c05c", justify="center", relief="flat", state="readonly")
canvas.create_window(250, 400, window = password_field)

screen.mainloop()

