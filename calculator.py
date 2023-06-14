import tkinter
from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.geometry("380x500+100+200")
root.resizable(False,False)
root.configure(bg="black")

Label_result= Label(root,width=25,height=2,text="",font=("Arial", 20))
Label_result.pack()

Button(root, text="C", width=5, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="#3697f5").place(x=10, y=100)

root.mainloop()

