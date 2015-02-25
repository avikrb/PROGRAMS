from tkinter import *
import tkinter
import sqlite3
from tkinter import messagebox


conn = sqlite3.connect("interview.sqlite")
conn_result=sqlite3.connect("results.sqlite")

cursor_result = conn_result.cursor()
cursor = conn.cursor()

def close_window (root): 
  root.destroy()

def sel():
    selection = "Your answer" + str(var.get())
    label.config(text = selection)

def sel2():
    selection = "Your  answer" + str(var2.get())
    label2.config(text = selection)

def quest():
    root = Tk()
    var = IntVar()
    label1 = Label(root, text="Which of the following is not an animal?")
    label1.pack(side=TOP)

    g1_1 = Radiobutton(root, text="Bat", variable=var, value=1,command=sel)
    g1_1.pack(side=TOP)
    g1_2 = Radiobutton(root, text="Cricket", variable=var, value=2,command=sel)
    g1_2.pack(side=TOP)
    g1_3 = Radiobutton(root, text="Hammer", variable=var, value=3,command=sel)
    g1_3.pack(side=TOP)
    label = Label(root)
    label.pack()
    root.mainloop()

def cmd():
    new_frame = Frame(Tk())
    welcome_msg = Frame(bottomframe)
    new_frame.pack(side = BOTTOM)
    l2 = Label(new_frame,text="Welcome "+str(e1.get()+"! Click Begin to get started"))
    l2.pack(side=LEFT)
    b2 = Button(new_frame,text="Begin", command=quest)
    b2.pack()
    



root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
l1 = Label(bottomframe, text="Enter you User Name")
l1.pack( side = LEFT)
e1 = Entry(bottomframe)
e1.pack(side = LEFT)
b1 = Button(bottomframe, text="Enter", command=cmd)
b1.pack()


root.mainloop()
'''
base = Tk()
base.title("User Input")
l1 = Label(base, text="Enter you User Name")
l1.pack( side = LEFT)
e1 = Entry(base)
e1.pack(side = LEFT)
b1 = Button(base, text="Enter", command=cmd)
b1.pack()

base.mainloop()
'''

'''
root = Tk()
var = IntVar()
g1_1 = Radiobutton(root, text="Group1 Option 1", variable=var, value=1,command=sel)
g1_1.pack(side=TOP)
g1_2 = Radiobutton(root, text="Group1 Option 2", variable=var, value=2,command=sel)
g1_2.pack(side=TOP)
g1_3 = Radiobutton(root, text="Groups1 Option 3", variable=var, value=3,command=sel)
g1_3.pack(side=TOP)

label = Label(root, text="Your selection will appear here")
label.pack(side=TOP)

var2 = IntVar()
g2_1 = Radiobutton(root, text="Group1 Option 1", variable=var2, value=10,command=sel2)
g2_1.pack(side=TOP)
g2_2 = Radiobutton(root, text="Group1 Option 2", variable=var2, value=20,command=sel2)
g2_2.pack(side=TOP)
g2_3 = Radiobutton(root, text="Groups1 Option 3", variable=var2, value=30,command=sel2)
g2_3.pack(side=TOP)

label2 = Label(root, text="Your second selection will appear here")
label2.pack(side=TOP)
root.mainloop()
'''
