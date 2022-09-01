from tkinter import *
from tkinter import messagebox
#from tkinterweb import HtmlFrame
from tkhtmlview import HTMLLabel

root=Tk()

root.title("Sportspedia")

root.geometry('1200x750')
root.maxsize(1200,750)

def clear(f):
    for w in f.winfo_children():
        w.destroy()

#frame1 - photo
f1=Frame(root,bg="skyblue",borderwidth=6)
f1.pack(side=TOP,fill="x")
photo=PhotoImage(file='sportspedia.png')
photo_label=Label(f1, image=photo)
photo_label.pack()
#frame -2 - drop downs
f2=Frame(root,bg="skyblue", width=250,borderwidth=6)
f2.pack_propagate(False)
f2.pack(side=LEFT, fill="y")

#frame 3 


#frame 4 - page display

#f4.pack(fill="both")
selfile="home"



#txtbox=Text(f4,width=950)


def save():
    filename=selfile+".txt"
    f=open(filename,'w')
    f.write(txtbox.get(1.0, END))
    f.close()
    txtbox.pack_forget()
    savebutton.pack_forget()
    file = open(filename)
    txt=file.read()
    htmllabel.set_html(txt)
    htmllabel.pack(fill="both", expand=True)
    
#savebutton = Button(f3,text="Save",command=save)


def homepage():
    f4=Frame(root)
    f4.pack(fill="both")
    #txtbox.pack_forget()
    savebutton.pack_forget()
    global selfile
    selfile="home"
    home=open("home.txt")
    hometxt=home.read()
    htmllabel=HTMLLabel(f4,background="white",height=450)
    htmllabel.set_html(hometxt)
    htmllabel.pack(fill="both", expand=True)
    #htmllabel.fit_height()


homepage()

def selected(event):
    txtbox.pack_forget()
    savebutton.pack_forget()
    global selfile
    selfile=clicked.get()
    filename = selfile +".txt"
    file = open(filename)
    txt=file.read()
    htmllabel.set_html(txt)
    htmllabel.pack(fill="both", expand=True)
    #htmllabel.fit_height()
    
    
#reading sports
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
    
    
dropdown()



def edit():
    
    htmllabel.pack_forget()
    txtbox.delete('1.0',END)
    filename=selfile+".txt"
    f=open(filename,'r')
    txt=f.read()
    txtbox.insert('end',txt)
    f.close()
    txtbox.pack()
    savebutton.pack()
    
def done():
    b1["state"]=NORMAL
    b2["state"]=NORMAL
    global answer 
    answer = messagebox.askyesno("Question","Do you want to save this file?")
    if answer == True:
        addfile()
    f3.destroy()
    homepage()
    
def cancel():
    f3.destroy()
    b1["state"]=NORMAL
    b2["state"]=NORMAL
    clear(f3)
    homepage()

def add():
    f3=Frame(root)
    f4.destroy()
    f3.pack(fill="both")
    b1["state"]=DISABLED
    b2["state"]=DISABLED
    global donebutton 
    donebutton = Button(f3,text="Done",command = done)
    donebutton.pack(side=RIGHT)
    global cancelbutton 
    cancelbutton= Button(f3,text="Cancel",command = cancel)
    cancelbutton.pack(side=RIGHT)
    global flabel
    flabel = Label(f3,text="Please write the new article's name that you want to add")
    flabel.pack()
    global fnametext
    fnametext=Text(f3,height=5,width = 950)
    fnametext.pack()
    global tlabel 
    tlabel= Label(f3,text="Please write the contents of your article")
    tlabel.pack()
    global txt
    txt=Text(f3)
    txt.pack()
    
def addfile():
    flabel.pack_forget()
    global fname
    fname=fnametext.get(1.0, END).strip()
    path="/Users/dharmishasharma/Desktop/Wiki project/"+fname+".txt"
    newfile=open(path,'w')
    newfile.write(txtbox.get(1.0, END))
    newfile.close()
    f=open('sports.txt','r')
    sname = f.read()
    sname+=", "+fname
    f.close()
    f=open('sports.txt','w')
    f.write(sname)
    f.close()
    flabel.pack_forget()
    fnametext.pack_forget()
    tlabel.pack_forget()
    donebutton.pack_forget()
    global opsfile
    opsfile=open("sports.txt",'r')
    drop.pack_forget()
    dropdown()
    homepage()
    
    


b2=Button(f1, text="Edit",command=edit)
b2.pack(side=RIGHT,padx=100)

b3=Button(f1, text="Add new",command=add)
b3.pack(side=RIGHT, padx=100)

b1=Button(f1, text="Home",command=homepage)
b1.pack(side=RIGHT,padx=100)




root.mainloop()
