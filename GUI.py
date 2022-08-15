from email import message
import tkinter
from tkinter import *
from tkinter import messagebox
print(tkinter)
root = tkinter.Tk()
root.title("GUI")
#setting width and height of GUI
root.geometry("600x600")
#Label
#label = tkinter.Label(root,text="Hello").pack()
#Button
'''b = Button(root,text = "Subscribe",bg="green",fg="white")
b.grid(column=1,row=0)
#radiobutton
r1 = Radiobutton(root,text ="Python",value=1)
r1.grid(column=2,row=1)
r2 = Radiobutton(root,text ="Java",value=2)
r2.grid(column=2,row=2)
r3 = Radiobutton(root,text ="C++",value=3)
r3.grid(column=2,row=3)
#Entry
t = Entry(root,width=50)
t.grid(column=3,row=0)'''
#Message
def Button1():
    messagebox.showinfo("Status","Please subscribe")
b = Button(root,text="Python Life",command=Button1)
b.pack()

root.mainloop()