from tkinter import *
from tkinter import messagebox
#from tkinterweb import HtmlFrame
from html_parser import HTMLLabel
from home import *
from Parse import *

def save(f,sf):
    filename_md="Markdown_Articles/"+sf+".md"
    f=open(filename_md,'w')
    f.write(txtbox.get(1.0, END))
    f.close()
    Parse_File(filename_md)
    #file = open(filename)
    #txt=file.read()
    savebutton.pack_forget()
    txtbox.config(state=DISABLED)
    messagebox.showinfo("Information","Congratulations! Your changes are saved!")
    txtbox.pack_forget()


def update(event):
    
    #print("update")
    t=txtbox.get(1.0,END)
    t_html=Parse_Markdown_str(t)
    htmllabel.set_html(t_html)
    #htmllabel.set_html(t_html)


def edit(f,sf):
    for w in f.winfo_children():
        w.destroy()
    
    global savebutton
    savebutton = Button(f,text="Save",command=lambda : save(f,sf))
    global txtbox
    txtbox=Text(f)
    global htmllabel
    htmllabel=HTMLLabel(f,background="white",width=450)
    htmllabel.pack()
    txtbox.delete('1.0',END)
    filename=sf+".md"
    f=open("Markdown_Articles/"+filename,'r')
    txt=f.read()
    txtbox.insert('end',txt)
    f.close()
    txtbox.pack()
    t=txtbox.get(1.0,END)
    t1_html=Parse_Markdown_str(t)
    htmllabel.set_html(t1_html)
    txtbox.bind("<Key>",update)
    savebutton.pack(side=BOTTOM)

