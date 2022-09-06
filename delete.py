from tkinter import *
from tkinter import messagebox
from tkinterweb import HtmlFrame
from html_parser import HTMLLabel
import os
from home import *

def delete(f,file):
    path_md="/Users/dharmishasharma/Desktop/Wiki project/Markdown_Articles/"+file+".md"
    if os.path.isfile(path_md):
        os.remove(path_md)
    path_html="/Users/dharmishasharma/Desktop/Wiki project/Html_Articles/"+file+".html"
    if os.path.isfile(path_html):
        os.remove(path_html)
    messagebox.showinfo("Information","The article has been removed")
    homepage(f)

