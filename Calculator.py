import tkinter as tk
from tkinter import *

# Create main application window
root = Tk()
root.title("Attractive Calculator")
root.geometry("400x600")
root.configure(bg="#2C3E50")

# Entry widget for the calculator display
entry = Entry(root, font=("Arial", 28), bd=10, relief=RIDGE, justify=RIGHT, bg="#ECF0F1")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=20)

# Functionality of the calculator
def button_click(value):
    entry.insert(END, value)

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Define button properties
button_bg = "#3498DB"
button_fg = "#FFFFFF"
button_font = ("Arial", 18, "bold")
button_width = 5
button_height = 2

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = Button(root, text=text, font=button_font, width=button_width, height=button_height, bg="#E74C3C", fg=button_fg, command=calculate)
    else:
        btn = Button(root, text=text, font=button_font, width=button_width, height=button_height, bg=button_bg, fg=button_fg, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Clear button
btn_clear = Button(root, text="C", font=button_font, width=button_width, height=button_height, bg="#F39C12", fg=button_fg, command=clear)
btn_clear.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

root.mainloop()
