from tkinter import *
from tkinter import messagebox
from tkhtmlview import HTMLLabel
from home import *
from dropdown import *

def cancel(f):
    homepage(f)


def addfile(n):
    path="/Users/dharmishasharma/Desktop/Wiki project/"+n+".txt"
    newfile=open(path,'w')
    newfile.write(txt.get(1.0, END))
    newfile.close()
    f=open('sports.txt','r')
    sname = f.read()
    sname+=", "+n
    f.close()
    f=open('sports.txt','w')
    f.write(sname)
    f.close() 
    

def add(n,f):
    for w in f.winfo_children():
        w.destroy()
    
    global donebutton 
    donebutton = Button(f,text="Done",command = lambda: [addfile(n),cancel(f)])
    donebutton.pack(side=RIGHT)
    """global cancelbutton 
    cancelbutton= Button(f,text="Exit",command=lambda :cancel(f))
    cancelbutton.pack(side=RIGHT)"""
    global tlabel 
    tlabel= Label(f,text="Please write the contents of your article")
    tlabel.pack()
    global txt
    txt=Text(f)
    txt.pack()
    addfile(n)