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

#TextBOX
def submit():
    comment=entry.get()
    print("comment:"+ comment)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete((len(entry.get()))-1,END)

global entry
entry= Entry(window,font=("Arial",50))
entry.insert(0,"leave a comment")
entry.pack(side=LEFT)

submit_button=Button(window,text="submit",command=submit)
submit_button.pack(side=LEFT)

delete_button=Button(window,text="delete",command=delete)
delete_button.pack(side=LEFT)

back_space=Button(window,text="back",command=backspace)
back_space.pack(side=LEFT)

#creating button + click & photo
count=0
def click():
    global count
    count+=1
    print(count,"likes")
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