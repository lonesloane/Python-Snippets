"""
4 demo classes run as independent program processes: multiprocessing;
multiprocessing allows us to launch named functions with arguments,
but not lambdas, because they are not pickleable on Windows (Chapter 5);
multiprocessing also has its own IPC tools like pipes for communication;
"""

from Tkinter import *
from multiprocessing import process

demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

def runDemo(modname):
    module = __import__(modname)
    module.Demo().mainloop()


if __name__ == '__main__':
    for modname in demoModules:
        process.Process(target=runDemo, args=(modname,)).start()

    root = Tk()
    root.title('Processes')
    Label(root, text='Multiple programs demo: multiprocessing', bg='white').pack()
    root.mainloop()