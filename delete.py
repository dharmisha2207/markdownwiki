from tkinter import *
from tkinter import messagebox
from tkinterweb import HtmlFrame
from tkhtmlview import HTMLLabel
import os
from home import *

def delete(f,file):
    path="/Users/dharmishasharma/Desktop/Wiki project/"+file+".txt"
    if os.path.isfile(path):
        os.remove(path)
    messagebox.showinfo("Information","The article has been removed")
    homepage(f)

