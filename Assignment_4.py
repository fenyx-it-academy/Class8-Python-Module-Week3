#Assignment_4

from tkinter import *  # import tkinter package.
import random   # import random method .

#defined, Interface for the user .
screen = Tk() 
title = screen.title("Generat a Random Password ")
canvas = Canvas(screen ,width=100 , height= 100 )
canvas.pack()

#define random values.
upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&**~`?/+-*/(){[]><}"


#function to generate the random value .
def generate():
     
    length_password = int(box1.get()) #bring the values from the interface.
    user_choice =  box2.get()


    if user_choice == "number": #conditions, for the user option.
        a = "".join(random.sample(numbers,length_password))
        print(a)
    elif user_choice == "uppercase":
        a = "".join(random.sample(upper_case_letters,length_password))
        print(a)
    elif user_choice == "lowercase":
        a = "".join(random.sample(lower_case_letters,length_password))
        print(a)  
    elif user_choice == "symbols":
        a = "".join(random.sample(symbols,length_password))
        print(a)  
    else : 
        a = "".join(random.sample((upper_case_letters + lower_case_letters + symbols + numbers),length_password))
        print(a) 
    box3.insert(0,a) #  this line displays the random password in the interface.  . 

def clear(): #function ,to clear every thing .
    box2.delete(0,END)
    box1.delete(0,END)
    box3.delete(0,END)

   
    
    



#create label
label_frame = LabelFrame(screen , text = "How many characters ? " )
label_frame.pack(pady = 10)

#create entry box 1

box1 = Entry(label_frame , font = ("Helvetica",24) )
box1.pack(pady = 10,padx = 10)



#create label2
label_frame2 = LabelFrame(screen , text = "please select one of those options : number , uppercase ,lowercase ,symbols or mix .  ")
label_frame2.pack(pady = 10)

#create entry box2 

box2 = Entry(label_frame2 , font = ("Helvetica",24) )
box2.pack(pady = 10,padx = 10)



#create label3
label_frame3 = LabelFrame(screen , text = '')
label_frame3.pack(pady = 20)


#create box3

box3 = Entry(screen , text = '',font = ("Helvetica",24),bd = 0,bg = "systembuttonface")
box3.pack(pady = 20)

#create buttons

frame2 = Frame(screen)
frame2.pack(pady = 10)

#create button1
button1 = Button(frame2 , text = "Generate Strong Password",command = generate)
button1.grid(row = 0, column = 0 ,padx = 10 )
#create button2
button2 = Button(frame2 , text ="clear",command  =clear)
button2.grid(row = 0, column = 1 ,padx = 10 )

screen.mainloop()