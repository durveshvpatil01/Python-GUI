from tkinter import *
import tkinter
root=Tk()

label1 = Label(root,text="Enter Username")
label2 = Label(root,text="Enter Password")

text1 = Entry(root)
text2 = Entry(root)

checkbox1 = Checkbutton(root, text="Keep Me Logged In")

button = Button(root,text="LoginIn")

label1.grid(row=0,column=0,sticky=E)
label2.grid(row=1,column=0,sticky=E)

text1.grid(row=0,column=1)
text2.grid(row=1,column=1)

checkbox1.grid(row=2,column=0,columnspan=2,sticky=E)

button.grid(row=3,column=0,columnspan=2,sticky=E+W)

root.mainloop();
