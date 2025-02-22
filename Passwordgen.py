import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive number")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Create main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#2C3E50")

# Header Label
header_label = tk.Label(root, text="Secure Password Generator", font=("Arial", 16, "bold"), bg="#2C3E50", fg="#ECF0F1")
header_label.pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#34495E", padx=20, pady=20)
frame.pack(pady=10)

# Input Label
input_label = tk.Label(frame, text="Enter password length:", font=("Arial", 12), bg="#34495E", fg="#ECF0F1")
input_label.pack()

# Entry Widget
entry = tk.Entry(frame, font=("Arial", 14), justify="center")
entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14, "bold"), bg="#E74C3C", fg="#FFFFFF", command=generate_password)
generate_button.pack(pady=10)

# Password Label
password_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#2C3E50", fg="#F1C40F", wraplength=350)
password_label.pack(pady=10)

# Run the application
root.mainloop()
