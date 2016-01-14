from Tkinter import *
from menu_frm import makeMenu

root = Tk()
for i in range(2):
    mnu = makeMenu(root)
    mnu.config(bd=2, relief=RAISED)
    Label(root, bg='black', height=5, width=25).pack(expand=YES, fill=BOTH)
Button(root, text='Bye', command=root.quit).pack(side=BOTTOM)
root.mainloop()