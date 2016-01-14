from Tkinter import *
from entry2 import makeform, fetch, fields

def show(entries, popup):
    fetch(entries)
    popup.destroy()

def ask():
    popup = Toplevel()  # show form in modal dialog window
    ents = makeform(popup, fields)
    Button(popup, text='OK', command=(lambda: show(ents, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()  # wait for destroy here

root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()
