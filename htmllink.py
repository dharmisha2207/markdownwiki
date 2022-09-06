from tkinter import *
from tkinter import messagebox
from tkinterhtml import HtmlFrame
from tkhtmlview import HTMLLabel


root=Tk()

f = Frame(root)
f.pack()
frame=HTMLLabel(f)

#open_in_browser_link = f"file://{os.path.join(folder, filename)}"

f=open("Html_Articles/htmltest.html")
t=f.read()
frame.set_html(t)
frame.pack()

root.mainloop()