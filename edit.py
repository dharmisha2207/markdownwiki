from tkinter import *
from tkinter import messagebox
#from tkinterweb import HtmlFrame
from tkhtmlview import HTMLLabel
from home import *

def save(f,sf):
    filename=sf+".txt"
    f=open(filename,'w')
    f.write(txtbox.get(1.0, END))
    f.close()
    file = open(filename)
    txt=file.read()
    savebutton.pack_forget()
    txtbox.config(state=DISABLED)
    messagebox.showinfo("Information","Congratulations! Your changes are saved!")

def update(file):
    f=open(file+".txt",'w')
    t=f.write(txtbox.get(1.0,END))
    #newtext.delete(1.0,END)
    #newtext.insert(1.0,t)"""

def edit(f,sf):
    for w in f.winfo_children():
        w.destroy()
    
    global savebutton
    savebutton = Button(f,text="Save",command=lambda : save(f,sf))
    global txtbox
    txtbox=Text(f)
    txtbox.delete('1.0',END)
    filename=sf+".txt"
    f=open(filename,'r')
    txt=f.read()
    """global newtext
    newtext=Text(f)
    newtext.insert(1.0,txt)
    newtext.pack()
    newtext.config(state=DISABLED)"""
    txtbox.insert('end',txt)
    f.close()
    txtbox.pack()
    txtbox.bind("<key>",update(sf))
    savebutton.pack()

