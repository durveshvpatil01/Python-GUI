from tkinter import *

master = Tk()

var = IntVar()
var1 = IntVar()
c = Checkbutton(master, text="c++", variable=var)
c.pack()
c = Checkbutton(master, text="java", variable=var1)
c.pack()

mainloop()
