__author__ = 'stephane'

from Tkinter import *

def greetings():
    print 'Hello stdout world'


win = Frame()
win.pack(side=TOP, expand=YES, fill=BOTH)

Button(win, text='Hello', command=greetings).pack(side=LEFT, fill=Y)
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT, fill=X, expand=TRUE)

win.mainloop()