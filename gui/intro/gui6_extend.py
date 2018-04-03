__author__ = 'stephane'

from Tkinter import *
from gui.intro.gui6_reusability import HelloFrame

class HelloExtender(HelloFrame):
    def make_widgets(self):
        HelloFrame.make_widgets(self)
        Button(self, text='Extend', command=sys.exit).pack(side=RIGHT)

    def message(self):
        print('hello', self.data)

if __name__ == '__main__':
    HelloExtender().mainloop()