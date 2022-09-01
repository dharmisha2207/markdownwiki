from tkinter import *
from tkinter import messagebox
from tkinterweb import HtmlFrame
from tkhtmlview import HTMLLabel

root=Tk()

lb = HTMLLabel(root)
lb.set_html("<a href 'www.google.com'> Google </a>"
lb.pack())

root.mainloop()