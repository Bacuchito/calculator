import pytest
from tkinter import Tk, Label, Button

def test_addition():
    root = Tk()
    equation = ""
    Label_result = Label(root, width=25, height=2, text="", font=("Arial", 20))
    Label_result.pack()

    def show(value):
        nonlocal equation
        equation += value
        Label_result.config(text=equation)

    def clear():
        nonlocal equation
        equation = ""
        Label_result.config(text=equation)

    def calculate():
        nonlocal equation
        result = ""
        if equation != "":
            try:
                result = eval(equation)
            except:
                result = "ERROR"
                equation = ""
        Label_result.config(text=result)

    # Test addition
    clear()
    show("5")
    show("+")
    show("3")
    calculate()
    result = Label_result.cget("text")
    assert result == 8

    clear()
    show("2")
    show("5")
    show("+")
    show("5")
    show("7")
    calculate()
    result = Label_result.cget("text")
    assert result == 82

def test_subtraction():
    root = Tk()
    equation = ""
    Label_result = Label(root, width=25, height=2, text="", font=("Arial", 20))
    Label_result.pack()

    def show(value):
        nonlocal equation
        equation += value
        Label_result.config(text=equation)

    def clear():
        nonlocal equation
        equation = ""
        Label_result.config(text=equation)

    def calculate():
        nonlocal equation
        result = ""
        if equation != "":
            try:
                result = eval(equation)
            except:
                result = "ERROR"
                equation = ""
        Label_result.config(text=result)

    # Test addition
    clear()
    show("9")
    show("2")
    show("-")
    show("4")
    show("8")
    calculate()
    result = Label_result.cget("text")
    assert result == 44

    clear()
    show("4")
    show("2")
    show("0")
    show("-")
    show("1")
    show("6")
    show("7")
    show("2")
    calculate()
    result = Label_result.cget("text")
    assert result == -1252

pytest.main()