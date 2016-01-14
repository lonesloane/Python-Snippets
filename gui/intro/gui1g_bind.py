__author__ = 'stephane'

from Tkinter import *
import sys

def hello(event):
    print 'Press twice to exit'

def quit(event):
    print 'Time to go...'
    sys.exit()

widget = Button(None, text='Hello event world!')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)
widget.mainloop()