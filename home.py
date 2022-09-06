from tkinter import *
from tkinter import messagebox
#from tkinterweb import HtmlFrame
from html_parser import HTMLLabel


#homeframe

global htmllabel


def homepage(f):
    for w in f.winfo_children():
        w.destroy()
    home=open("Html_Articles/home.html")
    hometxt=home.read()
    htmllabel=HTMLLabel(f,background="white",height=450)
    htmllabel.set_html(hometxt)
    htmllabel.pack(fill="both", expand=True)

