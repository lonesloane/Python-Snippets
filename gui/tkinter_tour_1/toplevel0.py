__author__ = 'stephane'

from Tkinter import *
import sys

win1 = Toplevel()
win2 = Toplevel()

Button(win1, text='Spam', command=sys.exit).pack()
Button(win2, text='Spaf', command=sys.exit).pack()

Label(text="Main window").pack()

win1.mainloop()