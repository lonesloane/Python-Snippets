__author__ = 'stephane'

from Tkinter import *
from gui.intro.gui6_reusability import HelloFrame


class HelloContainer(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        HelloFrame(self).pack(side=RIGHT)
        Button(self, text='Attach', command=sys.exit).pack(side=LEFT)

if __name__ == '__main__':
    HelloContainer().mainloop()