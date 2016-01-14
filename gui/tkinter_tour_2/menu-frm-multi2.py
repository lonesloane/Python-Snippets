from Tkinter import *
from menu_frm import makeMenu

root = Tk()
for i in range(3):
    frm = Frame()
    mnu = makeMenu(frm)
    mnu.config(bd=2, relief=RAISED)
    frm.pack(expand=YES, fill=BOTH)
    Label(frm, bg='black', height=5, width=25).pack(expand=YES, fill=BOTH)
Button(root, text='Bye', command=root.quit).pack(side=BOTTOM)
root.mainloop()