__author__ = 'stephane'

from Tkinter import *
import sys


class HelloClass:
    def __init__(self):
        widget = Button(None, text='Hello event world', command=self.quit)
        widget.pack()

    def quit(self):
        print('Hello class method World')
        sys.exit()

HelloClass()
mainloop()