import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

# Colors for Dark Theme
BG_COLOR = "#1e1e1e"
TEXT_COLOR = "#ffffff"
BUTTON_COLOR = "#333333"
HIGHLIGHT_COLOR = "#ff9800"

# File to store contacts
FILE_NAME = "contacts.csv"

# Ensure CSV file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email", "Address"])  # Column headers


# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter Name:")
    phone = simpledialog.askstring("Input", "Enter Phone Number:")
    email = simpledialog.askstring("Input", "Enter Email:")
    address = simpledialog.askstring("Input", "Enter Address:")

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone Number are required!")
        return

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email, address])

    refresh_contact_list()
    messagebox.showinfo("Success", "Contact Added!")


# Function to load and display contacts
def load_contacts():
    contacts_listbox.delete(0, tk.END)
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip headers
        for row in reader:
            contacts_listbox.insert(tk.END, f"{row[0]} - {row[1]}")


# Function to search contacts
def search_contact():
    query = simpledialog.askstring("Search", "Enter Name or Phone:")
    if not query:
        return

    contacts_listbox.delete(0, tk.END)
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if query.lower() in row[0].lower() or query in row[1]:
                contacts_listbox.insert(tk.END, f"{row[0]} - {row[1]}")


# Function to delete a contact
def delete_contact():
    selected = contacts_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a contact to delete.")
        return

    contact_name = contacts_listbox.get(selected).split(" - ")[0]
    updated_contacts = []

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] != contact_name:
                updated_contacts.append(row)

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email", "Address"])  # Headers
        writer.writerows(updated_contacts)

    refresh_contact_list()
    messagebox.showinfo("Success", "Contact Deleted!")


# Function to update a contact
def update_contact():
    selected = contacts_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a contact to update.")
        return

    contact_name = contacts_listbox.get(selected).split(" - ")[0]
    updated_contacts = []

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == contact_name:
                name = simpledialog.askstring("Update", "Enter New Name:", initialvalue=row[0])
                phone = simpledialog.askstring("Update", "Enter New Phone:", initialvalue=row[1])
                email = simpledialog.askstring("Update", "Enter New Email:", initialvalue=row[2])
                address = simpledialog.askstring("Update", "Enter New Address:", initialvalue=row[3])
                updated_contacts.append([name, phone, email, address])
            else:
                updated_contacts.append(row)

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email", "Address"])  # Headers
        writer.writerows(updated_contacts)

    refresh_contact_list()
    messagebox.showinfo("Success", "Contact Updated!")


# Function to refresh contact list
def refresh_contact_list():
    contacts_listbox.delete(0, tk.END)
    load_contacts()


# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x500")
root.config(bg=BG_COLOR)

# Title Label
title_label = tk.Label(root, text="📖 Contact Book", fg=HIGHLIGHT_COLOR, bg=BG_COLOR, font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Contact List
contacts_listbox = tk.Listbox(root, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Arial", 12), width=40, height=10)
contacts_listbox.pack(pady=10)

# Button Frame
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=10)


def create_button(text, command):
    return tk.Button(button_frame, text=text, font=("Arial", 10, "bold"), fg=TEXT_COLOR, bg=BUTTON_COLOR, width=12, height=2, command=command)


# Buttons
add_btn = create_button("Add Contact", add_contact)
search_btn = create_button("Search", search_contact)
update_btn = create_button("Update", update_contact)
delete_btn = create_button("Delete", delete_contact)

add_btn.grid(row=0, column=0, padx=5, pady=5)
search_btn.grid(row=0, column=1, padx=5, pady=5)
update_btn.grid(row=1, column=0, padx=5, pady=5)
delete_btn.grid(row=1, column=1, padx=5, pady=5)

# Load Contacts Initially
load_contacts()

# Run App
root.mainloop()
