import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.create_ui()

    def create_ui(self):
        self.result_label = tk.Label(self.root, text="Resultado:")
        self.result_label.pack()

        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(self.root, textvariable=self.result_var, state='readonly')
        self.result_entry.pack()

        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.pack()

        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.pack()

        self.operation_var = tk.StringVar()
        self.operation_var.set("Suma")
        self.operation_menu = tk.OptionMenu(self.root, self.operation_var, "Suma", "Resta", "Multiplicación", "División", "División Entera", "Módulo", "Potencia")
        self.operation_menu.pack()

        self.calculate_button = tk.Button(self.root, text="Calcular", command=self.calculate)
        self.calculate_button.pack()

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "Suma":
                result = num1 + num2
            elif operation == "Resta":
                result = num1 - num2
            elif operation == "Multiplicación":
                result = num1 * num2
            elif operation == "División":
                result = num1 / num2
            elif operation == "División Entera":
                result = num1 // num2
            elif operation == "Módulo":
                result = num1 % num2
            elif operation == "Potencia":
                result = num1 ** num2

            self.result_var.set(result)
        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
