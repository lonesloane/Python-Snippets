__author__ = 'stephane'

from Tkinter import *

root = Tk()
widget = Label(root)
widget.config(text='Oh, come on, you again?!?')
widget.pack(side=TOP, expand=YES, fill=BOTH)
root.title('Big Foot')
root.mainloop()