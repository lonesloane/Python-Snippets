__author__ = 'stephane'

from Tkinter import *
import tkinter102


# main app window
mainWin = Tk()
Label(mainWin, text=__name__).pack()

# popup window
popup = Toplevel()
Label(popup, text='attach').pack(side=LEFT)
tkinter102.MyGui(popup).pack(side=RIGHT)

mainWin.mainloop()
