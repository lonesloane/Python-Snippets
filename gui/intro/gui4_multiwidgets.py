__author__ = 'stephane'

from Tkinter import *

def greetings():
    print('Hello stdout world')


win = Frame()
win.pack()

Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Hello', command=greetings).pack(side=LEFT)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)

win.mainloop()