from mainmodule import *
from tkinterview import *

def hyperlink(url,f):
    for w in f.winfo_children():
        w.destroy()
    file.open(url)
    txt=file.read()
    
    htmllabel=HTMLLabel(f,background="white",height=450)
    htmllabel.set_html(txt)
    #htmllabel.on_link_click
    htmllabel.pack(fill="both", expand=True)
    