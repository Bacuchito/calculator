import pytest
from tkinter import Button, Label
from calculator import show, clear, calculate


@pytest.fixture
def calculator_app():
    import tkinter as tk
    from calculator import show, clear, calculate

    root = tk.Tk()
    root.title("Simple Calculator")
    root.geometry("380x430+100+200")
    root.resizable(False, False)
    root.configure(bg="black")

    equation = ""

    Label_result = Label(root, width=25, height=2, text="", font=("Arial", 20))
    Label_result.pack()

    Button(root, text="C", width=4, height=1, font=("Arial", 20, "bold"), bd=1, fg="#fff", bg="#3697f5",
           command=lambda: clear()).place(x=17, y=80)
    Button(root, text="7", width=4, height=1, font=("Arial", 20, "bold"), bd=1, fg="#fff", bg="Gray",
           command=lambda: show("7")).place(x=17, y=150)
    Button(root, text="8", width=4, height=1, font=("Arial", 20, "bold"), bd=1, fg="#fff", bg="Gray",
           command=lambda: show("8")).place(x=107, y=150)
    Button(root, text="+", width=4, height=1, font=("Arial", 20, "bold"), bd=1, fg="#fff", bg="Red",
           command=lambda: show("+")).place(x=287, y=290)
    Button(root, text="=", width=4, height=1, font=("Arial", 20, "bold"), bd=1, fg="#fff", bg="Orange",
           command=lambda: calculate()).place(x=287, y=360)

    yield root

    root.destroy()


def test_calculator_addition(calculator_app):
    button_7 = calculator_app.children["!button2"]
    button_8 = calculator_app.children["!button3"]
    button_add = calculator_app.children["!button4"]
    button_equals = calculator_app.children["!button5"]

    button_7.invoke()
    button_add.invoke()
    button_8.invoke()
    button_equals.invoke()

    label_result = calculator_app.children["!label"]
    assert label_result.cget("text") == "15"


def test_calculator_subtraction(calculator_app):
    button_7 = calculator_app.children["!button2"]
    button_8 = calculator_app.children["!button3"]
    button_add = calculator_app.children["!button4"]
    button_equals = calculator_app.children["!button5"]

    button_7.invoke()
    button_add.invoke()
    button_8.invoke()
    button_equals.invoke()

    button_subtract = calculator_app.children["!button4"]
    button_5 = calculator_app.children["!button6"]

    button_subtract.invoke()
    button_5.invoke()
    button_equals.invoke()

    label_result = calculator_app.children["!label"]
    assert label_result.cget("text") == "10"


def test_calculator_multiplication(calculator_app):
    button_7 = calculator_app.children["!button2"]
    button_8 = calculator_app.children["!button3"]
    button_add = calculator_app.children["!button4"]
    button_equals = calculator_app.children["!button5"]

    button_7.invoke()
    button_add.invoke()
    button_8.invoke()
    button_equals.invoke()

    button_multiply = calculator_app.children["!button4"]
    button_2 = calculator_app.children["!button6"]

    button_multiply.invoke()
    button_2.invoke()
    button_equals.invoke()

    label_result = calculator_app.children["!label"]
    assert label_result.cget("text") == "30"


def test_calculator_division(calculator_app):
    button_7 = calculator_app.children["!button2"]
    button_8 = calculator_app.children["!button3"]
    button_add = calculator_app.children["!button4"]
    button_equals = calculator_app.children["!button5"]

    button_7.invoke()
    button_add.invoke()
    button_8.invoke()
    button_equals.invoke()

    button_divide = calculator_app.children["!button4"]
    button_2 = calculator_app.children["!button6"]

    button_divide.invoke()
    button_2.invoke()
    button_equals.invoke()

    label_result = calculator_app.children["!label"]
    assert label_result.cget("text") == "7.5"
