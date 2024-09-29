# import tkinter as tk
# import math

# # Functionality of the calculator
# def on_button_click(value):
#     current_text = display.get()
#     display.delete(0, tk.END)
#     display.insert(tk.END, current_text + str(value))

# def on_clear():
#     display.delete(0, tk.END)

# def on_calculate():
#     try:
#         expression = display.get()
#         result = eval(expression)  # Evaluate the mathematical expression
#         display.delete(0, tk.END)
#         display.insert(tk.END, str(result))
#     except:
#         display.delete(0, tk.END)
#         display.insert(tk.END, "Error")

# # Memory function placeholders
# memory = 0

# def on_memory_clear():
#     global memory
#     memory = 0

# def on_memory_recall():
#     display.delete(0, tk.END)
#     display.insert(tk.END, str(memory))

# def on_memory_add():
#     global memory
#     try:
#         memory += float(display.get())
#         display.delete(0, tk.END)
#     except:
#         display.delete(0, tk.END)
#         display.insert(tk.END, "Error")

# def on_memory_subtract():
#     global memory
#     try:
#         memory -= float(display.get())
#         display.delete(0, tk.END)
#     except:
#         display.delete(0, tk.END)
#         display.insert(tk.END, "Error")

# # Main window
# root = tk.Tk()
# root.title("Shop Calculator")
# root.geometry("350x600")  # Adjust size to simulate shop calculators

# # Outer frame for border and style
# outer_frame = tk.Frame(root, bg="black", bd=10)  # Black border for a shop-like look
# outer_frame.pack(expand=True, fill='both', padx=10, pady=10)

# # Inner frame for buttons and display
# inner_frame = tk.Frame(outer_frame, bg="gray", bd=5)  # Dark inner frame with slight border
# inner_frame.pack(expand=True, fill='both')

# # Display Entry
# display = tk.Entry(inner_frame, font=('Arial', 30, 'bold'), borderwidth=10, relief=tk.SUNKEN, bg="white", fg="black", justify='right')
# display.pack(fill=tk.BOTH, padx=10, pady=10)

# # Frame for buttons
# button_frame = tk.Frame(inner_frame, bg="gray")
# button_frame.pack(expand=True, fill='both')

# # Standard buttons
# buttons = [
#     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#     ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
# ]

# # Memory buttons (Shop calculators often have memory functions)
# memory_buttons = [
#     ('MC', 0, 0, on_memory_clear), ('MR', 0, 1, on_memory_recall),
#     ('M+', 0, 2, on_memory_add), ('M-', 0, 3, on_memory_subtract)
# ]

# # Create standard buttons and assign their respective functions
# for (text, row, col) in buttons:
#     if text == '=':
#         btn = tk.Button(button_frame, text=text, font=('Arial', 20, 'bold'), bg="lightgreen", fg="black", relief=tk.RAISED, borderwidth=4, command=on_calculate)
#     elif text == 'C':
#         btn = tk.Button(button_frame, text=text, font=('Arial', 20, 'bold'), bg="lightcoral", fg="black", relief=tk.RAISED, borderwidth=4, command=on_clear)
#     else:
#         btn = tk.Button(button_frame, text=text, font=('Arial', 20, 'bold'), bg="lightblue", fg="black", relief=tk.RAISED, borderwidth=4, command=lambda t=text: on_button_click(t))
#     btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# # Create memory buttons
# for (text, row, col, command) in memory_buttons:
#     btn = tk.Button(button_frame, text=text, font=('Arial', 20, 'bold'), bg="orange", fg="black", relief=tk.RAISED, borderwidth=4, command=command)
#     btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# # Configure rows and columns to expand proportionally
# for i in range(5):  # Adjusted to accommodate extra memory buttons
#     button_frame.grid_rowconfigure(i, weight=1)
# for i in range(4):
#     button_frame.grid_columnconfigure(i, weight=1)

# # Start the Tkinter main loop
# root.mainloop()
import tkinter as tk

# Functionality of the calculator
def on_button_click(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + str(value))

def on_clear():
    display.delete(0, tk.END)

def on_calculate():
    try:
        expression = display.get()
        result = eval(expression)  # Evaluate the mathematical expression
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")  # Set a more defined window size

title_label=tk.Label(root,text="CALCULATOR",font=("Times",30,'bold'),bd=20)
title_label.pack(padx=10,pady=20)
title_label.config(fg="red")

# Outer frame for full border
outer_frame = tk.Frame(root, bg="grey", bd=20)  # Thick black border around the calculator
outer_frame.pack(expand=True, fill='both', padx=10, pady=10)  # Expand to cover the window


# Inner frame for buttons and display (white background)
inner_frame = tk.Frame(outer_frame, bg="black", bd=10)  # Inner white frame
inner_frame.pack(expand=True)

# Display Entry
display = tk.Entry(inner_frame, font=('Arial', 30, 'bold'), borderwidth=5, relief=tk.SUNKEN, bg="lightgray", fg="black", justify='right')
display.pack(fill=tk.BOTH, padx=10, pady=10)

# Frame for buttons
button_frame = tk.Frame(inner_frame, bg="black")
button_frame.pack(expand=True, fill='both')

# Standard buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create standard buttons and assign their respective functions
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(button_frame, text=text, font=('Times', 20, 'bold'), bg="lightgreen", fg="black", relief=tk.RAISED, borderwidth=4, command=on_calculate)
    elif text == 'C':
        btn = tk.Button(button_frame, text=text, font=('Times', 20, 'bold'), bg="lightcoral", fg="black", relief=tk.RAISED, borderwidth=4, command=on_clear)
    else:
        btn = tk.Button(button_frame, text=text, font=('Times', 20, 'bold'), bg="lightblue", fg="black", relief=tk.RAISED, borderwidth=4, command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Configure rows and columns to expand proportionally
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

# Start the Tkinter main loop
root.mainloop()
