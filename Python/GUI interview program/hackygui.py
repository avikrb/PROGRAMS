from tkinter import *
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect("interview.sqlite")
conn_result=sqlite3.connect("results.sqlite")

cursor_result = conn_result.cursor()
cursor = conn.cursor()

global count
global USERNAME
count = 0

def cmd():
    pass    
 #   USERNAME = str(e1.get())
    
    

color1="#CCFFFF"
color2="#CCFFCC"

root = Tk()
root.title("Technical Interview Questions")
#root["bg"]=color1
#text=color2
#highlightbackground=color2
result = cursor.execute("select * from interview_questions")
count = 0
total = 0
QUESTIONS = []
OPTIONS = []
ANSWERS=[]

for row in result:
    total +=1
    QUESTIONS.append(row[0])
    
    row_1 = row[1].split(",")
    OPTIONS.append(row_1)
    ANSWERS.append(row[2])
#    choice = input ("Your answer: ")
#    choice = int(choice)-1
#    if row_1[int(choice)] == row[2]:
#        count = count + 1
        

def quitapp():
    root.destroy()

frame = Frame(root, width=1650, height=875)
frame.focus_set()
result = cursor.execute("select * from interview_questions")
l1 = Label(frame, text="Enter you User Name")
l1.pack( side = TOP)
e1 = Entry(frame)
e1.pack(side = LEFT)

b1 = Button(frame, text="Enter", command=cmd)
username=e1.get()
b1.pack()


def sel1():
   if (var.get() == 1):
       ++count
   selection = "You selected the option " + str(var.get())
   labelS1.config(text = selection)

def sel2():
   if (var.get() == 30):
       ++count
   selection = "You selected the option " + str(var.get())
   labelS1.config(text = selection)

def sel3():
   selection = "You selected the option " + str(var.get())
   labelS1.config(text = selection)

def sel4():
   selection = "You selected the option " + str(var.get())
   labelS1.config(text = selection)

def sel11():
   if (var2.get() == 1):
       ++count
   selection = "You selected the option " + str(var2.get())
   labelS2.config(text = selection)

def sel22():
   if (var2.get() == 30):
       ++count
   selection = "You selected the option " + str(var2.get())
   labelS2.config(text = selection)

def sel33():
   selection = "You selected the option " + str(var2.get())
   labelS2.config(text = selection)

def sel44():
   selection = "You selected the option " + str(var2.get())
   labelS2.config(text = selection)

   
def hide_me(event):
    event.widget.grid_forget()

def callback_and_hide():
    count = 0
    user_name = str(e1.get())
    user_name = "Sammy"
    total = 2
 #   user_name = USERNAME
    choice1 = int(var.get()) -1
    if ANSWERS[0] == OPTIONS[0][choice1]:
        count += 1

    choice2 = int(var2.get()) -1
    if ANSWERS[1] == OPTIONS[1][choice2]:
        count += 1
    if ((count/total)*100) >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
        
    interview_results = [(user_name,count, total, grade)]


    cursor_result.executemany("insert into interview_results(username,correct,total,pass_fail) values(?,?,?,?)",interview_results)
    conn_result.commit()
    conn_result.close()
    conn.close()
        
    pass
    #button.bind('<Button-1>',hide_me) 
    #button.grid_forget()


labelS = Label(root,height = 4, text="PLEASE SELECT ALL POSSILE ANSWERS? IMPORTANT ONLY SUBMITTED ANSWERS WILL BE COUNTED!")
labelS.pack(side=TOP)

var = IntVar()
labelQ1 = Label(root, text=QUESTIONS[0])
labelQ1.pack(side=TOP)
g1_1 = Radiobutton(root, text=OPTIONS[0][0], variable=var, value=1,command=sel1)
g1_1.pack(side=TOP)
g1_2 = Radiobutton(root, text=OPTIONS[0][1], variable=var, value=2,command=sel2)
g1_2.pack(side=TOP)
g1_3 = Radiobutton(root, text=OPTIONS[0][2], variable=var, value=3,command=sel3)
g1_3.pack(side=TOP)
g1_4 = Radiobutton(root, text=OPTIONS[0][3], variable=var, value=4,command=sel4)
g1_4.pack(side=TOP)

labelS1= Label(root, height = 4,text="Your selection will appear here")
labelS1.pack(side=TOP)





var2 = IntVar()
labelQ2 = Label(root, text=QUESTIONS[1])
labelQ2.pack(side=TOP)
g2_1 = Radiobutton(root, text=OPTIONS[1][0], variable=var2, value=1,command=sel11)
g2_1.pack(side=TOP)
g2_2 = Radiobutton(root, text=OPTIONS[1][1], variable=var2, value=2,command=sel22)
g2_2.pack(side=TOP)
g2_3 = Radiobutton(root, text=OPTIONS[1][2], variable=var2, value=3,command=sel33)
g2_3.pack(side=TOP)
g2_4 = Radiobutton(root, text=OPTIONS[1][3], variable=var2, value=4,command=sel44)
g2_4.pack(side=TOP)

labelS2 = Label(root,height = 1, text="Your selection will appear here")
labelS2.pack(side=TOP)


button1 = Button(root,   
	highlightbackground=color2,text="SUBMIT YOUR RESPONSE!", command= callback_and_hide())
button1.pack()




button = Button(root, text="click to Quit", command=quitapp)
button.pack()


frame.pack()
root.mainloop()
