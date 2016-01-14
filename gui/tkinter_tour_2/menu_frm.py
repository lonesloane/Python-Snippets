from Tkinter import *
import tkMessageBox

def notdone():
    tkMessageBox.showerror('Not implemented', 'Not yet available')


def makeMenu(parent):
    menuBar = Frame(parent)
    menuBar.pack(side=TOP, fill=X)

    fButton = Menubutton(menuBar, text='File', underline=0)
    fButton.pack(side=LEFT)
    file = Menu(fButton)
    file.add_command(label='New...', command=notdone, underline=0)
    file.add_command(label='Open...', command=notdone, underline=0)
    file.add_command(label='Quit...', command=parent.quit, underline=0)
    fButton.config(menu=file)

    eButton = Menubutton(menuBar, text='Edit', underline=0)
    eButton.pack(side=LEFT)
    edit = Menu(eButton)
    edit.add_command(label='Cut', command=notdone, underline=0)
    edit.add_command(label='Paste', command=notdone, underline=0)
    edit.add_separator()
    eButton.config(menu=edit)

    subMenu = Menu(edit, tearoff=FALSE)
    subMenu.add_command(label='Spam', command=notdone, underline=0)
    subMenu.add_command(label='Eggs', command=notdone, underline=0)
    edit.add_cascade(label='Stuff', menu=subMenu, underline=0)

    return menuBar

if __name__ == '__main__':
    root = Tk()
    root.title('menu_frm')
    makeMenu(root)
    msg = Label(root, text='Frame menu basics')
    msg.pack(expand=YES, fill=BOTH)
    msg.config(relief=SUNKEN, width=40, height=7, bg='beige')
    root.mainloop()

