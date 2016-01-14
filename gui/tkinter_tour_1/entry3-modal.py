#  Can fetch values after destroy with stringVars

from Tkinter import *
from entry3 import makeform, fetch, fields

def show(variables, popup):
    popup.destroy()  # order of destroy does not matter anymore
    fetch(variables)


def ask():
    popup = Toplevel()  # form in modal mode
    vars = makeform(popup, fields)
    Button(popup, text='OK', command=(lambda: show(vars, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()  # wait for destroy here

root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()
