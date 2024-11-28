import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle button clicks
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the calculation
entry = tk.Entry(root, width=20, font=('Arial', 18), bd=5, relief=tk.SUNKEN, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
    ('=', 5, 0)
]

# Add buttons to the GUI
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=32, height=2, font=('Arial', 12),
                        command=evaluate_expression)
        btn.grid(row=row, column=col, columnspan=4)
    elif text == "C":
        btn = tk.Button(root, text=text, width=8, height=2, font=('Arial', 12),
                        command=clear_entry)
        btn.grid(row=row, column=col)
    else:
        btn = tk.Button(root, text=text, width=8, height=2, font=('Arial', 12),
                        command=lambda t=text: button_click(t))
        btn.grid(row=row, column=col)

# Run the application
root.mainloop()
