__author__ = 'stephane'

from Tkinter import *
from gui.intro.gui6_reusability import HelloFrame

parent = Frame(None)
parent.pack()
HelloFrame(parent).pack(side=RIGHT)

Button(parent, text='Attach', command=sys.exit).pack(side=LEFT)

parent.mainloop()