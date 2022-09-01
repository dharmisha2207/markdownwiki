from tkinter import *
from tkinter import messagebox
#from tkinterweb import HtmlFrame
from tkhtmlview import HTMLLabel


def selected(event):
    global selfile
    selfile=clicked.get()
    filename = selfile +".txt"
    file = open(filename)
    txt=file.read()
    htmllabel.set_html(txt)
    htmllabel.pack(fill="both", expand=True)

def dropdown(f):
    for w in f.winfo_children():
        w.destroy()
    opsfile=open("sports.txt",'r')
    ops=opsfile.read()
    sportslist=ops.split(", ")
    global clicked
    clicked=StringVar()
    clicked.set("Choose your genre of sports")
    global drop 
    global htmllabel
    htmllabel=HTMLLabel(f,background="white",height=450)
    drop=OptionMenu(f, clicked, *sportslist ,command=selected)
    drop.pack()

