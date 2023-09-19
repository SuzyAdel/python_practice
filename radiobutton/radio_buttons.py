from tkinter import *
window = Tk()
def chioce():
    if (x.get()==0):
        print('will take to c window')
    else:
        print("will take tto py window")
options=['c languge','python']
x=IntVar()

c = PhotoImage(file = 'c.png')
pyth = PhotoImage(file = 'python.png')
photos=[c,pyth]

for index in range(len(options)):
    radiobutton = Radiobutton(window, text=options[index],
                              variable=x,value=index,
                              font=('impact',50),
                              image=photos[index],compound=LEFT,
                              command=chioce)
    radiobutton.pack(anchor=W)

window.mainloop()