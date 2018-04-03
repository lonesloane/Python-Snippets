"create a bar of check buttons that run dialog demos"

from Tkinter import *
from dialogtable import demos
from quitter import Quitter

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        self.tools()
        Label(self, text='Check demos').pack()
        self.vars = []
        for key in demos:
            var = IntVar()
            Checkbutton(self, text=key, variable=var, command=demos[key]).pack(side=LEFT)
            self.vars.append(var)

    def report(self):
        for var in self.vars:
            print(var.get(),)
        print(' ')

    def tools(self):
        fm = Frame(self)
        fm.pack(side=RIGHT)
        Button(fm, text='State', command=self.report).pack(fill=X)
        Quitter(fm).pack(fill=X)

if __name__ == '__main__':
    Demo().mainloop()