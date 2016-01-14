__author__ = 'stephane'

from Tkinter import *

root = Tk()
labelfont = ('times', 20, 'bold')
widget = Label(root, text='Hello config world')
widget.config(bg='black', fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=20)
widget.pack(expand=YES, fill=BOTH)
root.mainloop()
