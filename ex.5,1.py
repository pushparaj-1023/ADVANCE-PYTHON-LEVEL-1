from tkinter import *

root=Tk()
root.title("STUDENT MARK LIST")
root.geometry("500x700")

l=Label(root,text="USER NAME")
l.pack()

e=Entry(root)
e.pack()

b=Button(root,text="LOGIN")
b.pack()

root.mainloop()

