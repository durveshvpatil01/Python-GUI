from tkinter import *
import tkinter
root=Tk()

root.iconbitmap(r'C:\Users\Abhi\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7')

label1 = Label(root,text="Enter Username")
label2 = Label(root,text="Enter Password")

text1 = Entry(root,bd=4)
text2 = Entry(root,bd=4)

checkbox1 = Checkbutton(root, text="Keep Me Logged In")

button = Button(root,text="LoginIn",relief=GROOVE)

label1.grid(row=0,column=0,sticky=E)
label2.grid(row=1,column=0,sticky=E)

text1.grid(row=0,column=1)
text2.grid(row=1,column=1)

checkbox1.grid(row=2,column=0,columnspan=2,sticky=E)

button.grid(row=3,column=0,columnspan=2,sticky=E+W)

root.mainloop();
