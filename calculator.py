import tkinter
from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("380x430+100+200")
root.resizable(False, False)
root.configure(bg="black")

equation = ""

def show(value):
    global equation
    equation+=value
    Label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    Label_result.config(text=equation)

def percentage():
    global equation
    equation += "%"
    Label_result.config(text=equation)

def square():
    global equation
    equation += "**2"
    Label_result.config(text=equation)

def delete():
    global equation
    equation = equation[:-1]
    Label_result.config(text=equation)

def calculate():
    global equation
    result =""
    if equation !="":
        try:
            equation = equation.replace("%", "/100")
            result = eval(equation)
        except:
            result = "ERROR"
            equation = ""
    Label_result.config(text=result)
    

Label_result= Label(root,width=25,height=2,text="",font=("Arial", 20))
Label_result.pack()

Button(root, text="C", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=17, y=80)
Button(root, text="%", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Red", command=lambda: percentage()).place(x=107, y=80)
Button(root, text="x²", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Red", command=lambda: square()).place(x=197, y=80)
Button(root, text="/", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Red", command=lambda: show("/")).place(x=287, y=80)

Button(root, text="7", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Gray", command=lambda: show("7")).place(x=17, y=150)
Button(root, text="8", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Gray", command=lambda: show("8")).place(x=107, y=150)
Button(root, text="9", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Gray", command=lambda: show("9")).place(x=197, y=150)
Button(root, text="*", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Red", command=lambda: show("*")).place(x=287, y=150)

Button(root, text="4", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Gray", command=lambda: show("4")).place(x=17, y=220)
Button(root, text="5", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Gray", command=lambda: show("5")).place(x=107, y=220)
Button(root, text="6", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Gray", command=lambda: show("6")).place(x=197, y=220)
Button(root, text="-", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Red", command=lambda: show("-")).place(x=287, y=220)

Button(root, text="1", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Gray", command=lambda: show("1")).place(x=17, y=290)
Button(root, text="2", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Gray", command=lambda: show("2")).place(x=107, y=290)
Button(root, text="3", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Gray", command=lambda: show("3")).place(x=197, y=290)
Button(root, text="+", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Red", command=lambda: show("+")).place(x=287, y=290)

Button(root, text=".", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Gray", command=lambda: show(".")).place(x=17, y=360)
Button(root, text="0", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Gray", command=lambda: show("0")).place(x=107, y=360)
Button(root, text="<-", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Gray", command=lambda: delete()).place(x=197, y=360)
Button(root, text="=", width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg="Orange", command=lambda: calculate()).place(x=287, y=360)


root.mainloop()

