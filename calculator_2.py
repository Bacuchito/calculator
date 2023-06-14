import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        # Creating a Screen 
        self.screen = tk.Entry(master, width=25, font=('Arial', 16))
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Crear los botones
        self.create_button("x²", 1, 0,)
        self.create_button("%", 1, 1)
        self.create_button("/", 1, 2)
        self.create_button("<-", 1, 3)

        self.create_button("7", 2, 0)
        self.create_button("8", 2, 1)
        self.create_button("9", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("4", 3, 0)
        self.create_button("5", 3, 1)
        self.create_button("6", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("1", 4, 0)
        self.create_button("2", 4, 1)
        self.create_button("3", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button(".", 5, 0)
        self.create_button("0", 5, 1)
        self.create_button("C", 5, 2)
        self.create_button("=", 5, 3)

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 16),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.screen.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.screen.get())
                self.screen.delete(0, tk.END)
                self.screen.insert(0, str(result))
            except:
                self.screen.delete(0, tk.END)
                self.screen.insert(0, "Error")
        elif text == "x²":
            try:
                result = float(self.screen.get()) ** 2
                self.screen.delete(0, tk.END)
                self.screen.insert(0, str(result))
            except:
                self.screen.delete(0, tk.END)
                self.screen.insert(0, "Error")
        elif text == "%":
            try:
                result = float(self.screen.get()) / 100
                self.screen.delete(0, tk.END)
                self.screen.insert(0, str(result))
            except:
                self.screen.delete(0, tk.END)
                self.screen.insert(0, "Error")
        elif text == "<-":
            self.screen.delete(len(self.screen.get())-1, tk.END)
        else:
            self.screen.insert(tk.END, text)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
