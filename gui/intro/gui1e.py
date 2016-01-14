__author__ = 'stephane'

from Tkinter import *


def quit():
    print("Bye, I have to go now...")
    sys.exit()

def handler(A, B):
    print "Bye {0} {1}, I hope to see you again soon...".format(A, B)
    sys.exit()


widget = Button(None,
                text='Click me, I dare you!',
                command=(lambda: handler('Lone', 'Sloane')) )
widget.pack()
widget.mainloop()