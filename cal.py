# import tkinter as tk
# root=tk.Tk()
# root.title("CALCULATOR")

# title_label=tk.Label(root,text="CALCULATOR",font=('Times', 40))
# title_label.pack()

# frame=tk.Frame(root)
# frame.pack()



# button1=tk.Button(frame,text="1",font=('Times',30),bg="red")
# button1.grid(row=0,column=0)

# button2=tk.Button(frame,text="2",font=('Times',30),bg="red")
# button2.grid(row=0,column=1)

# button3=tk.Button(frame,text="3",font=('Times',30),bg="red")
# button3.grid(row=0,column=2)

# buttonP=tk.Button(frame,text="+",font=('Times',30),bg="red")
# buttonP.grid(row=0,column=3)

# button4=tk.Button(frame,text="4",font=('Times',30),bg="red")
# button4.grid(row=1,column=0)

# button5=tk.Button(frame,text="5",font=('Times',30),bg="red")
# button5.grid(row=1,column=1)

# button6=tk.Button(frame,text="6",font=('Times',30),bg="red")
# button6.grid(row=1,column=2)


# buttonm=tk.Button(frame,text="-",font=('Times',30),bg="red")
# buttonm.grid(row=1,column=3)

# button7=tk.Button(frame,text="7",font=('Times',30),bg="red")
# button7.grid(row=2,column=0)

# button8=tk.Button(frame,text="8",font=('Times',30),bg="red")
# button8.grid(row=2,column=1)

# button9=tk.Button(frame,text="9",font=('Times',30),bg="red")
# button9.grid(row=2,column=2)

# buttons=tk.Button(frame,text="*",font=('Times',30),bg="red")
# buttons.grid(row=2,column=3)

# buttonz=tk.Button(frame,text="0",font=('Times',30),bg="red")
# buttonz.grid(row=3,column=0)


# buttonc=tk.Button(frame,text="click",font=('Times',30),bg="red")
# buttonc.grid(row=3,column=1)

# buttone=tk.Button(frame,text="=",font=('Times',30),bg="red")
# buttone.grid(row=3,column=2)

# buttond=tk.Button(frame,text="/",font=('Times',30),bg="red")
# buttond.grid(row=3,column=3)









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
root.title("CALCULATOR")

# Display
display = tk.Entry(root, font=('Times', 40), borderwidth=5, relief=tk.RIDGE, justify='right')
display.pack(fill=tk.BOTH, padx=10, pady=10)

# Frame for buttons
frame = tk.Frame(root)
frame.pack()

# Button creation
buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('+', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('/', 3, 3)
]

# Create buttons and assign commands
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(frame, text=text, font=('Times', 30), bg="green", command=on_calculate)
    elif text == 'C':
        btn = tk.Button(frame, text=text, font=('Times', 30), bg="red", command=on_clear)
    else:
        btn = tk.Button(frame, text=text, font=('Times', 30), bg="red", command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, sticky="nsew")

# Make the buttons expand to fill space
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
for i in range(4):
    frame.grid_rowconfigure(i, weight=1)

# Run the main loop
root.mainloop()
