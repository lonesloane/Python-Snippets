__author__ = 'stephane'

from Tkinter import *
import tkMessageBox


def callback():
    if tkMessageBox.askyesno('Verify', 'Do you really want to quit?'):
        tkMessageBox.showwarning('Yes', 'Quit not yet implemented')
    else:
        tkMessageBox.showinfo('No', 'Quit has been cancelled')

errmsg = 'Sorry, no spam allowed!'
Button(text='Quit', command=callback).pack(fill=Y)
Button(text='Spam', command=(lambda: tkMessageBox.showerror('Spam', errmsg))).pack(fill=X)
mainloop()