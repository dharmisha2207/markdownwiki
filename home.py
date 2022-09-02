from tkinter import *
from tkinter import messagebox
#from tkinterweb import HtmlFrame
from tkhtmlview import HTMLLabel


#homeframe

global htmllabel


def homepage(f):
    for w in f.winfo_children():
        w.destroy()
    home=open("home.html")
    hometxt=home.read()
    htmllabel=HTMLLabel(f,background="white",height=450)
    htmllabel.set_html(hometxt)
    htmllabel.pack(fill="both", expand=True)

