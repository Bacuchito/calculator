import tkinter as tk
from tkinter import *

def create_button(root, text, command, x, y, bg):
    return Button(root, text=text, width=4, height=1, font=("Arial",20,"bold"), bd=1, fg="#fff", bg=bg, command=command).place(x=x, y=y)

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

Label_result= Label(root, width=25, height=2, text="", font=("Arial", 20))
Label_result.pack()

create_button(root, "C", clear, 17, 80, "#3697f5")
create_button(root, "%", percentage, 107, 80, "red")
create_button(root, "x²", square, 197, 80, "red")
create_button(root, "/", lambda: show("/"), 287, 80, "red")

create_button(root, "7", lambda: show("7"), 17, 150, "gray")
create_button(root, "8", lambda: show("8"), 107, 150, "gray")
create_button(root, "9", lambda: show("9"), 197, 150, "gray")
create_button(root, "*", lambda: show("*"), 287, 150, "red")

create_button(root, "4", lambda: show("4"), 17, 220, "gray")
create_button(root, "5", lambda: show("5"), 107, 220, "gray")
create_button(root, "6", lambda: show("6"), 197, 220, "gray")
create_button(root, "-", lambda: show("-"), 287, 220, "red")

create_button(root, "1", lambda: show("1"), 17, 290, "gray")
create_button(root, "2", lambda: show("2"), 107, 290, "gray")
create_button(root, "3", lambda: show("3"), 197, 290, "gray")
create_button(root, "+", lambda: show("+"), 287, 290, "red")

create_button(root, ".", lambda: show("."), 17, 360, "gray")
create_button(root, "0", lambda: show("0"), 107, 360, "gray")
create_button(root, "<-", delete, 197, 360, "gray")
create_button(root, "=", calculate, 287, 360, "orange")

root.mainloop()
