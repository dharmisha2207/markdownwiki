from tkinter import *
from tkinter import messagebox
#from tkinterweb import HtmlFrame
from tkhtmlview import HTMLLabel
from add import *

root=Tk()

root.title("Sportspedia")

root.geometry('1200x750')
root.maxsize(1200,750)



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

#frame 3 - page display
f3=Frame(root)


selfile="home"

htmllabel=HTMLLabel(f3,background="white",height=450)

txtbox=Text(f3,width=950)


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
    
savebutton = Button(f3,text="Save",command=save)


def homepage():
    txtbox.pack_forget()
    savebutton.pack_forget()
    global selfile
    selfile="home"
    home=open("home.txt")
    hometxt=home.read()
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
    global answer 
    answer = messagebox.askyesno("Question","Do you want to save this file?")
    if answer == True:
        addfile()
    

    
def addfile():
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

b3=Button(f1, text="Add new",command=add(f3,htmllabel))
b3.pack(side=RIGHT, padx=100)

b1=Button(f1, text="Home",command=homepage)
b1.pack(side=RIGHT,padx=100)




    


f3.pack(fill="both")


root.mainloop()
