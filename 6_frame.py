from tkinter import *

root = Tk()

frametop = Frame(root)
frametop.pack(side = TOP)

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frametop, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frametop, text="Brown", fg="orange")
greenbutton.pack( side = LEFT )

bluebutton = Button(bottomframe, text="Blue", fg="blue")
bluebutton.pack( side = BOTTOM )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()
