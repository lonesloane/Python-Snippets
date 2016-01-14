__author__ = 'stephane'

from Tkinter import *
import Tkinter

Tkinter.NoDefaultRoot()

win1 = Tk()
win2 = Tk()

Button(win1, text='Spam', command=win1.destroy).pack()
Button(win2, text='Spaf', command=win2.destroy).pack()

win1.mainloop()



