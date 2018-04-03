from Tkinter import *

root = Tk()
var = IntVar(0)  # select 0 to start
for i in range(10):
    rad = Radiobutton(root, value=i, variable=var, text=str(i))
    rad.pack(side=LEFT)
root.mainloop()
print( var.get())