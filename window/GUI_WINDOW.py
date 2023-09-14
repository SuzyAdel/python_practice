from tkinter import *

window= Tk()
window.geometry("420x420")
window.title("Suzy's 1st GUI program")


icon= PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")

photo= PhotoImage(file='person.png')
label=Label(window,text="Hello World, LETS START CODING!",
            font=('Arial',40,'bold'),
            fg='blue',bg="white",
            relief=RAISED,bd=10,
            padx=20,pady=20,
            image= photo, 
            compound='top')  #fg=foreground of lable, bd border width

label.pack() #puts anywhere
#label.place(x=100,y=100), cordinates 

window.mainloop()