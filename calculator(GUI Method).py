import tkinter as tk

def calculate(operation):
    try:
        num1_val = float(num1_var.get())
        num2_val = float(num2_var.get())

        if operation == "add":
            result.set(num1_val + num2_val)
        elif operation == "subtract":
            result.set(num1_val - num2_val)
        elif operation == "multiply":
            result.set(num1_val * num2_val)
        elif operation == "divide":
            if num2_val == 0:
                result.set("Error! Division by zero.")
            else:
                result.set(num1_val / num2_val)
    except ValueError:
        result.set("Error!")

root = tk.Tk()
root.title("Professional Calculator")
root.configure(bg="#f0f0f0")

num1_label = tk.Label(root, text="Enter first number:", font=("Helvetica", 12), bg="#f0f0f0")
num1_label.grid(row=0, column=0, padx=10, pady=10)
num1_var = tk.StringVar()
num1 = tk.Entry(root, textvariable=num1_var, font=("Helvetica", 12))
num1.grid(row=0, column=1, padx=10, pady=10)

num2_label = tk.Label(root, text="Enter second number:", font=("Helvetica", 12), bg="#f0f0f0")
num2_label.grid(row=1, column=0, padx=10, pady=10)
num2_var = tk.StringVar()
num2 = tk.Entry(root, textvariable=num2_var, font=("Helvetica", 12))
num2.grid(row=1, column=1, padx=10, pady=10)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.grid(row=2, columnspan=2, pady=(20, 0))

add_button = tk.Button(button_frame, text="Add", command=lambda: calculate("add"), font=("Helvetica", 12), bg="#4CAF50", fg="white")
add_button.grid(row=0, column=0, padx=5)

subtract_button = tk.Button(button_frame, text="Subtract", command=lambda: calculate("subtract"), font=("Helvetica", 12), bg="#2196F3", fg="white")
subtract_button.grid(row=0, column=1, padx=5)

multiply_button = tk.Button(button_frame, text="Multiply", command=lambda: calculate("multiply"), font=("Helvetica", 12), bg="#FF9800", fg="white")
multiply_button.grid(row=0, column=2, padx=5)

divide_button = tk.Button(button_frame, text="Divide", command=lambda: calculate("divide"), font=("Helvetica", 12), bg="#F44336", fg="white")
divide_button.grid(row=0, column=3, padx=5)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Helvetica", 14, "bold"), bg="#f0f0f0")
result_label.grid(row=3, columnspan=2, pady=(20, 10))

root.mainloop()
