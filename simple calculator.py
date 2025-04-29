import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()

        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            if num2 == 0:
                result.set("Error (div by 0)")
            else:
                result.set(num1 / num2)
        else:
            result.set("Invalid op")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
tk.Label(root, text="First Number").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Operator dropdown
tk.Label(root, text="Operation").grid(row=2, column=0)
operator = tk.StringVar(root)
operator.set("+")  # default value
tk.OptionMenu(root, operator, "+", "-", "*", "/").grid(row=2, column=1)

# Calculate button
tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

# Result display
result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=4, column=0)
tk.Label(root, textvariable=result).grid(row=4, column=1)

# Start the GUI loop
root.mainloop()
