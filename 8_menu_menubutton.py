from tkinter import *

root = Tk()

menubar = Menu(root)

filemenu = Menu(menubar,tearoff=0)

# add commands to menu
filemenu.add_command(label="New File")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)    


#menu button
mb=  Menubutton( root, text="File", relief=RAISED )
mb.pack()

mb.menu  =  Menu(mb, tearoff = 0)
mb["menu"]  =  mb.menu

mb.menu.add_command(label="New File")
mb.menu.add_command(label="Open")


root.mainloop()
