from tkinter import *
from tkinter import messagebox
from tkinterweb import HtmlFrame
from tkhtmlview import HTMLLabel
from tkinter import messagebox
from home import *
from edit import *
from add import *
from delete import *
from tkinter.simpledialog import askstring
#from dropdown import *

#root
root=Tk()
root.title("Sportspedia")
root.geometry('1200x750')
root.maxsize(1200,750)

#Frame 1 - photo and buttons( add, home, edit)

f1=Frame(root,bg="skyblue",borderwidth=6)
f1.pack(side=TOP,fill="x")
photo=PhotoImage(file='sportspedia.png')
photo_label=Label(f1, image=photo)
photo_label.pack()


#Frame 2 - dropdown

f2=Frame(root,bg="skyblue", width=250,borderwidth=6)
f2.pack_propagate(False)
f2.pack(side=LEFT, fill="y")


#Frame 3 - mainpage

f3 = Frame(root)
f3.pack(fill="both")


selfile = "home"

listbox=Listbox(f2)
listbox.configure(background='skyblue',fg='black',borderwidth=2)

def remove():
    f=open("sports.txt")
    t=f.read().split(", ")
    t.remove(selfile)
    final=t[0]
    for i in range(1,len(t)):
        final = final + ", " + t[i]
    f.close()
    f=open("sports.txt",'w')
    f.write(final)
    listbox.delete(index)

"""def selected(event):
    
    for w in f3.winfo_children():
        w.destroy()
    global selfile
    selfile=clicked.get()
    filename = selfile +".txt"
    file = open(filename)
    txt=file.read()
    htmllabel=HTMLLabel(f3,background="white",height=450)
    htmllabel.set_html(txt)
    htmllabel.pack(fill="both", expand=True)
    deletebut.bind("<Button 1>", remove()) 

def dropdown():
    opsfile=open("sports.txt",'r')
    ops=opsfile.read()
    sportslist=ops.split(", ")
    global clicked
    clicked=StringVar()
    clicked.set("Choose your genre of sports")
    global drop 
    drop=OptionMenu(f2, clicked, *sportslist ,command=selected)
    drop.pack()

dropdown()"""
lb = Label(f2,text="Select your choice of sport",bg='skyblue', font =("Arial", 15),fg='black',borderwidth=2,relief='solid')
lb.pack()


def items_selected(event):
    l=open("sports.txt")
    l1=l.read()
    sl=l1.split(", " )
    global selfile
    global index
    ind=listbox.curselection()
    index=ind[0]
    selfile=sl[index]
    f=open(selfile+".txt")
    txt=f.read()
    f.close()
    for w in f3.winfo_children():
        w.destroy()
    htmllabel=HTMLLabel(f3,background="white",height=450)
    htmllabel.set_html(txt)
    htmllabel.pack(fill="both", expand=True)
    
listbox.bind('<<ListboxSelect>>', items_selected)

l=open("sports.txt")
l1=l.read()
sl=l1.split(", " )
for i in range(0,len(sl)):
    listbox.insert(i,sl[i])

listbox.pack()
#frame 1 - buttons

def addlist():
    name = askstring('File Name', 'Please enter the file name')
    if name in sl:
            messagebox.showwarning("show warning", "File already exists!")
            cancel(f3)
    else:
        answer = messagebox.askyesno("Question","Do you want to continue?")
        if answer ==True:
            add(name,f3)
            listbox.insert(END,name)
        else:
            cancel(f3)


def setselfile():
    global selfile
    selfile = "home"

editb=Button(f1, text="Edit",command = lambda: edit(f3,selfile))
editb.pack(side=RIGHT,padx=100)

addb=Button(f1, text="Add new",command=addlist)
addb.pack(side=RIGHT, padx=100)

homeb=Button(f1, text="Home",command = lambda : [homepage(f3), setselfile()])
homeb.pack(side=RIGHT,padx=100)

deletebut=Button(f1,text="Remove",command=lambda:[delete(f3,selfile),remove()])
deletebut.pack(side=RIGHT)
#deletebut.bind("<Button 1>", remove)

homepage(f3)

root.mainloop()