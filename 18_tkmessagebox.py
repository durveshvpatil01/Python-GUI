from tkinter import *

top = Tk()

def hello():
   messagebox.showinfo("Say Hello", "Hello World")

B1 = Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()
