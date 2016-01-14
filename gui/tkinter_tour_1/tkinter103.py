__author__ = 'stephane'

from Tkinter import *
import tkMessageBox


def reply(name):
    tkMessageBox.showinfo(title='Reply', message='Hello %s!' % name)

top = Tk()
top.title('Echo')

Label(top, text='Enter your name:').pack(side=LEFT)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text='Submit', command=(lambda: reply(ent.get())))
btn.pack(side=RIGHT)

top.mainloop()