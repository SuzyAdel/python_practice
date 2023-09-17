from tkinter import *

window= Tk()#init window
window.geometry("420x420")
window.title("Suzy's 1st GUI program")


icon= PhotoImage(file='logo.png')#creating logo as icon photo
window.iconphoto(True,icon)
window.config(background="#5cfcff")

photo= PhotoImage(file='person.png') #adding a label and main photo
label=Label(window,text="LETS START CODING!",
            font=('Arial',40,'bold'),
            fg='blue',bg="white",
            relief=RAISED,bd=10,
            padx=20,pady=20,
            image= photo, 
            compound='top')  #fg=foreground of lable, bd border width

label.pack() #puts anywhere
#label.place(x=100,y=100), cordinates

#creating button + click & photo
count=0
def click():
    global count
    count+=1
    print(count)
photo2=PhotoImage(file="like.png")
button=Button(window,text="Like button",command=click,
              font=("comic Sans",30),
              fg="#f2d40c",bg="black",
              activeforeground="#f2d40c",
              activebackground="#f20c87",
              state=ACTIVE,
              image=photo2, compound=BOTTOM)
button.pack()


window.mainloop()