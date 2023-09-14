from tkinter import *

window= Tk()
window.geometry("420x420")
window.title("Suzy's 1st GUI program")

icon= PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop()