"""
4 demo classes in independent top-level windows;
not processes: when one is quit all others go away, because all windows run in
the same process here; make Tk() first here, else we get blank default window
"""

from Tkinter import *

demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']

def makePopups(modnames):
    demoObjects = []
    for modname in modnames:
        module = __import__(modname)
        window = Toplevel()  # make a new window
        demo = module.Demo(window)
        window.title(module.__name__)
        demoObjects.append(demo)
    return demoObjects

def allStates(demoObjects):
    for obj in demoObjects:
        print obj.__module__ + ':'
        if hasattr(obj, 'report'):
            obj.report()
        else:
            print 'none'

root = Tk()
root.title('Popups')
demos = makePopups(demoModules)
Label(root, text='Multiple top level windows demo', bg='white').pack()
Button(root, text='States', command=(lambda: allStates(demos))).pack(fill=X)
root.mainloop()