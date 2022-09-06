from tkinter import *
from tkinter import messagebox
from html_parser import HTMLLabel
from home import *
from Parse import *

def cancel(f):
    homepage(f)


def addfile(n):
    path="Markdown_Articles/"+n+".md"
    newfile=open(path,'w')
    newfile.write(txt.get(1.0, END))
    newfile.close()
    Parse_File(path)
    

    f=open('sports.txt','r')
    sname = f.read()
    l=sname.split(", ")
    l.append(n)
    l.sort()
    names=l[0]
    for i in range(1,len(l)):
        names=names+", "+l[i]
    f.close()
    f=open("sports.txt",'w')
    f.write(names)
    f.close()
    messagebox.showinfo("showinfo", "Article successfully added")

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