from Tkinter import *
from dialogtable import demos
from quitter import Quitter

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text='Radio demo').pack(side=TOP)
        self.var = StringVar()  # variable shared between all radio buttons
        for key in demos:
            Radiobutton(self,
                        text=key,
                        command=self.onPress,
                        variable=self.var,
                        value=key).pack(anchor=NW)
        self.var.set(key)  # select last to start
        Button(self, text='State', command=self.report).pack(fill=X)
        Quitter(self).pack(fill=X)

    def onPress(self):
        pick = self.var.get()
        print 'You pressed', pick
        print 'result: ', demos[pick]()

    def report(self):
        print self.var.get()

if __name__ == '__main__':
    Demo().mainloop()