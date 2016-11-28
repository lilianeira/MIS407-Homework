from tkinter import *
from tkinter.ttk import *

window = Tk()
weatherbtn = Button(window, text="Weather", width=12)
weatherbtn.grid(row = 1, column = 0)

busbtn = Button(window, text="Bus", width=12)
busbtn.grid(row = 1, column = 1)

sportbtn = Button(window, text="Sports", width=12)
sportbtn.grid(row = 2, column = 0)

newsbtn = Button(window, text="News", width=12)
newsbtn.grid(row = 2, column = 1)

window.mainloop()
#if pressed, update module by requesting new data
